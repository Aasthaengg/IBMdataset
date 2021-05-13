n, t = map(int, input().split())
tt = list(map(int, input().split()))

x = 0
for i in range(n-1):
  if tt[i] + t < tt[i+1]:
    x += tt[i+1] - (tt[i] + t)
print(tt[-1] + t - x)