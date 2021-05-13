N=int(input())
*A,=map(int,input().split())

if min(A)==0:
  print(0)
  exit()

ans = 1
for i in range(N):
  ans *= A[i]
  if ans > 10**18:
    print(-1)
    exit()
    
print(ans)