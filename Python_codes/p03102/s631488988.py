N,M,C=map(int,input().split())
B=list(map(int,input().split()))
ans=0
for i in range(N):
  A=list(map(int,input().split()))
  D=[A[k]*B[k] for k in range(M)]
  if sum(D)+C>0 :
    ans+=1
print(ans)
