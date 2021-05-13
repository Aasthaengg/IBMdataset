N=int(input())
K=int(input())
A=list(map(int,input().split()))
s=0
for i in range(N):
  s+=min(A[i],K-A[i])*2
print(s)