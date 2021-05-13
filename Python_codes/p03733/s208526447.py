N,T=map(int,input().split())
*S,=map(int,input().split())

ans=0
for i in range(1,len(S)):
    ans+=min(S[i]-S[i-1], T)
ans+=T
print(ans)