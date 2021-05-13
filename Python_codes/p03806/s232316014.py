from fractions import Fraction
import sys
input = sys.stdin.readline

INF = float('inf')

N,A,B = list(map(int,input().split()))
data = [list(map(int, input().split())) for _ in range(N)]

P = []
M = []
Z = []
for a,b,c in data:
  if Fraction(a,b) == Fraction(A,B):
    Z.append(c)
  elif Fraction(a,b) > Fraction(A,B):
    P.append((a*2520-b*2520*A//B,c))
  else:
    M.append((-a*2520+b*2520*A//B,c))
    
dpP = [INF for i in range(1000000)]
dpP[0] = 0
for v,c in P:
  for i in range(1000000)[::-1]:
    if i>=v:
      dpP[i] = min(dpP[i],dpP[i-v]+c)

dpM = [INF for i in range(1000000)]
dpM[0] = 0
for v,c in M:
  for i in range(1000000)[::-1]:
    if i>=v:
      dpM[i] = min(dpM[i],dpM[i-v]+c)
      
ans = INF
if Z:
  ans = min(Z)
for i in range(1,1000000):
  ans = min(ans,dpP[i]+dpM[i])

if ans == INF:
  print(-1)
else:
  print(ans)