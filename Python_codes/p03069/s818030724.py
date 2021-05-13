N=int(input())
S=input()
cnt=0
black=[0]*N
white=[0]*N
for i in range(N):
    if S[i]==".":
        white[i]=1
    else:
        black[i]=1
    if i>=1:
        white[i]+=white[i-1]
        black[i]+=black[i-1]
        
B=black[-1]
W=white[-1]

ans=min(B,W)
for i in range(1,N):
    num=black[i-1]+W-white[i-1]
    ans=min(ans,num)
    
print(ans)