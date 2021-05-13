N = int(input())
A = list(map(int, input().split()))
ans =1;
iszero = False

if 0 in A:
  iszero = True
for i in range(N):
  if(iszero):
    ans = 0
    break
  ans *= A[i] 
  if ans>10**18:
    ans = -1
    break

print(ans)