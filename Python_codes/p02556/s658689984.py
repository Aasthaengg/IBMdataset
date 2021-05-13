import random

N = int(input())
x = [0]*N
y = [0]*N
for i in range(N):
  x[i], y[i] = map(int, input().split())

minn = 10**10
maxn = -10**10
minp = 10**10
maxp = -10**10

for i in range(N):
  minn = min(minn, x[i]-y[i])
  maxn = max(maxn, x[i]-y[i])
  minp = min(minp, x[i]+y[i])
  maxp = max(maxp, x[i]+y[i])

print(max(maxn-minn, maxp-minp))
