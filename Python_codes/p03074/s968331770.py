N,K=map(int,input().split())
S=list(map(int,input()))
c1=[]
c0=[]
count=0
if S[0]==0:
    c1.append(0)
for i in range(N-1):
    count=count+1
    if S[i]!=S[i+1]:
        if S[i]==1:
            c1.append(count)
        else:
            c0.append(count)
        count=0
count=count+1
if S[N-1]==1:
    c1.append(count)
else:
    c0.append(count)
    c1.append(0)
if len(c0)<=K:
    print(N)
else:
    ans0=sum(c0[:K])
    ans1=sum(c1[:K+1])
    ans=ans0+ans1
    for i in range(len(c0)-K):
        ans0=ans0-c0[i]+c0[i+K]
        ans1=ans1-c1[i]+c1[i+K+1]
        ans=max(ans,ans0+ans1)
    print(ans)