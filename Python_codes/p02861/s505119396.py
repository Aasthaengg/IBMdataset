import math
N = int(input())
xy = []
l = []
def comb(n,k):
  if n < k:
    n, K = k, N
  nu = 1
  de = 1
  for i in range(k):
    nu *= (N - i)
    de *= (K-i)
  return nu // de

for i in range(N):
  xy.append(list(map(int, input().split())))
for i in range(N-1):
  for j in range(i+1,N):
    l.append(math.sqrt((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1]) ** 2))

nu = math.factorial(N-2) * (N - 1) * 2
de = math.factorial(N)
ans = sum(l) * nu / de
print(ans)