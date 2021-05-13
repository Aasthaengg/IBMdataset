"""

ある試合(a,b)が行われるまでに消化しておくべき試合を管理して、それが0になった組からキューに積む
みたいな感じで雑にやるとTLEが取れなかった。


LeetCodeのTwoSum的に、
a -> bで試合ができない場合は、情報を残しておいて、b -> a が回ってきた時に試合が実施されるようにするとよいっぽい
"""
from collections import deque

N = int(input())
match_order = [deque(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]


q = deque(range(N))
finish_by = [0] * N
next_opponent = [None] * N

while q:
    a = q.popleft()
    # aの残りの順で一番初めに戦う対戦相手を取り出す
    b = match_order[a].popleft()
    # 互いの初めに戦うべき相手がお互いであれば、そのペアで試合を行う
    if next_opponent[b] == a:
        # a,bが今までに試合した回数の多いほう+1（同じ人が日に二度試合を行えないので）
        finish_by[a] = finish_by[b] = max(finish_by[a], finish_by[b]) + 1
        # a,bについて、まだ対戦相手が残っているならキューに積む
        if match_order[a]:
            q.append(a)
        if match_order[b]:
            q.append(b)
    # bの残りの順で一番初めに戦う相手がaではないなら、順番が来るまで待つ
    # このあと(b,c)の試合が行われて、キューにb,cが積まれるとかで、aがbと試合するとかがあれば、消化される
    else:
        next_opponent[a] = b

# 対戦相手が残っている人がいる場合、条件通りに終わることができない
if any(match_order):
    print(-1)
else:
    print(max(finish_by))