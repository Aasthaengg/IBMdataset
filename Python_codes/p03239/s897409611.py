N, T = list(map(int,input().split()))
c = [0 for i in range(N)]
t = [0 for i in range(N)]
for i in range(N):
  c[i], t[i] = input().split()
  c[i] = int(c[i])
  t[i] = int(t[i])

ans = float('inf')
for i in range(N):
  if t[i] <= T and c[i] < ans:
    ans = c[i]
if ans == float('inf'):
  print('TLE')
else:
  print(ans)