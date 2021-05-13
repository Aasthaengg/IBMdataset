N = int(input())
Ts = list(map(int, input().split()))
As = list(map(int, input().split()))
c = 0
Hmax = [0]*N
Hmin = [1]*N
for i in range(N):
  T = Ts[i]
  Hmax[i] = T
  if T > c:
    Hmin[i] = T
    c = T
c = 0
for i in reversed(range(N)):
  A = As[i]
  Hmax[i] = min(Hmax[i], A)
  if A > c:
    Hmin[i] = max(Hmin[i], A)
    c = A
#print(Hmax)
#print(Hmin)
r = 1
for i in range(N):
  d = Hmax[i]-Hmin[i]+1
  if d < 0: d = 0
  r = r*d%1000000007
print(r)
