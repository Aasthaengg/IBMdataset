N,T=map(int,input().split())
A=list(map(int,input().split()))
ans=0
max_=0
B=[0]*N
for i in reversed(range(N)):
    B[i]=max(B[i],max_-A[i])
    max_=max(max_,A[i])
m=max(B)
print(B.count(m))