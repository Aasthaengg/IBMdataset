"""
愚直に考えると、
・今XXX日目です
・試合できる人は試合をします。
・その日一回でも試合があれば次の日に進んで、なかったらおわり
をやる。愚直にやろうとすると、
・各選手について、次に試合する相手
・各選手がその日に試合したかどうか（１日に同じ人が複数回試合できないので）
・現在XXX日目
などの情報を持つ必要があり、また、その日の終わりに、各選手が試合したかどうかなどから、その日１回でも試合があったか判定をしたり、処理がめんどくさい。

ちょっとひねった方法で考えると、
・各選手が順番に、自分が次に試合するべき相手を一人指名して場にカードを出す。
・マッチングが成立する（a->b, b->a のカードが両方場に出される）と、その試合が実施され、試合した二人の選手について、次に試合したい選手がいれば、またカードを場に出す
・aとbが試合した時の最短の日にちは、max(aが最後に試合した日, bが最後に試合した日)+1 で表される
・各選手がカードを出したにも関わらず、マッチングが成立しない場合は、与えられた順番で試合ができない。

の形で管理すると、今日は何日で～とか、その日一回でも試合があったか～とかを管理しなくてよい。
"""

from collections import deque

N = int(input())
A = [deque(list(map(int, input().split()))) for _ in range(N)]


q = deque()
for i in range(N):
    q.append(i)

next_game_with = [-1] * N
end_by = [0] * N
while q:
    a = q.popleft()
    opponent = A[a].popleft() - 1
    if next_game_with[opponent] == a:
        end_by[a] = end_by[opponent] = max(end_by[a], end_by[opponent]) + 1
        if A[a]:
            q.append(a)
        if A[opponent]:
            q.append(opponent)
    else:
        next_game_with[a] = opponent

finished = True
for i in range(N):
    if A[i]:
        finished = False
        break
if finished:
    print(max(end_by))
else:
    print(-1)