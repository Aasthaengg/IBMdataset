import sys
input = sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

nK=len(bin(K))-2
nA=len(bin(max(A)))-2
n=max(nK,nA)

p=[1]*(n+1)
for i in range(n):
    p[i+1]=p[i]*2

XX=[0]*n
temp=0

#calcX
for i in range(nK-1,-1,-1):
    cnt=0
    for j in range(N):
        if A[j]&p[i]==p[i]:#i桁目を見る
            cnt+=1
    if cnt<N-cnt:
        if temp+p[i]<=K:
            XX[i]=1
            temp+=p[i]
    
ans=0
for i in range(N):
    ans+=temp^A[i]
    
print(ans)