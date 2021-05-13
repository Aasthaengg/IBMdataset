def solve(B,G,x):
  sums = 0
  for i in range(N):
    req = B[i] - x//G[i] 
    sums += max(0,req)
  if sums <= K:
    return True
  else:
    return False

N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
A.sort(reverse=True)
F.sort()

if sum(A) <= K:
  print("0")
  exit(0)

L = []
MAX = 0
for i in range(N):
  temp = A[i]*F[i]
  MAX = max(MAX,temp)
ng = 1
ok = MAX+1
while abs(ng-ok) > 1:
  mid = (ok+ng)//2
  #print(mid,solve(A,F,mid))
  if solve(A,F,mid):
    ok = mid
  else:
    ng = mid
print(ok)
  
