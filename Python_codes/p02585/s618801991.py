# 解答

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
  P[i] -= 1  

visit = [False for _ in range(N)]
loops = []

for i in range(N):
  if visit[i]:
    continue
  now = i
  loop = [C[now]]
  visit[now] = True
  while not visit[P[now]]:
    now = P[now]
    loop.append(C[now])
    visit[now] = True
  loops.append(loop)

ans = -float("inf")
for loop in loops:
  n = len(loop)
  r = K%n
  m = K//n
  if r==0:
    r = n
    m -= 1
  suml = sum(loop)
  if K > n and suml <= 0:
    r = n
    m = 0
  cumsum = [0] + loop + loop[:r-1]
  for i in range(n+r-1):
    cumsum[i+1] = cumsum[i] + cumsum[i+1]
  maxC = -float("inf")
  for i in range(n):
    for j in range(i+1, i+r+1):
      maxC = max(maxC, cumsum[j]-cumsum[i])
  ans = max(ans, maxC + suml*m)
print(ans)