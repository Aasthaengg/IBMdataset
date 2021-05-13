N,K=map(int,input().split())
S=list(input())
ans=0
lr=0
rl=0
for i in range(N-1):
    if S[i]=="L":
        if S[i+1]=="R":
            lr=lr+1
        else:
            ans=ans+1
    else:
        if S[i+1]=="L":
            rl=rl+1
        else:
            ans=ans+1
change=max(rl,lr)
ans=ans+2*min(change,K)
print(min(ans,N-1))