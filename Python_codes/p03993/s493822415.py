p = int(input())
ans = 0
*A,= map(int,input().split())
for j,i in enumerate(A):
  if A[A[j]-1]==j+1:
    ans+=1
print(ans//2)