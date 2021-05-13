from collections import deque

N = int(input())
FF = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -10**10
q = deque()
q.append([])
while q:
  x = q.pop()
  if len(x) == 10:
    tmp = 0
    i = 0
    while i < N:
      tmp += P[i][sum([x[j]*FF[i][j] for j in range(10)])]
      i += 1
    ans = max(ans, -10**10 if sum(x) < 1 else tmp)
  else:
    q.append(x+[0])
    q.append(x+[1])
print(ans)