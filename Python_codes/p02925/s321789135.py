

from collections import deque


N = int(input())
A = [deque(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]


next_vs = [None] * N
day_finished = [0] * N
q = deque()
for i in range(N):
    q.append(i)

"""
・試合したらそいつらをキューに積む
・試合できなかったら、次はこいつと戦いたいよリストにいれる

キューを全て確認したのに、　次はこいつと戦いたいよリストが残っている/未試合の相手が残っている　状態であれば、与えられた順では試合ができない
"""

while q:
    x = q.popleft()
    opp_x = A[x].popleft()

    if next_vs[opp_x] == x:
        day_finished[x] = day_finished[opp_x] = max(day_finished[x], day_finished[opp_x]) + 1
        if A[x]:
            q.append(x)
        if A[opp_x]:
            q.append(opp_x)

    else:
        next_vs[x] = opp_x

for i in range(N):
    if A[i]:
        print(-1)
        exit()


print(max(day_finished))