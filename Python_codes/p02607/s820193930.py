N=int(input())
A=list(map(int,input().split()))
n=len(A)
k=0
ans=0
while 2*k+1 <=n:
  m=k*2
  if A[m] % 2 ==1:
    ans+=1
  k+=1
print(ans)