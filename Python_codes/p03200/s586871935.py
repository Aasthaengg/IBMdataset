S=input()
ans=0
cnt=S.count('B')
l=len(S)
for i in range(l):
    if S[i]=='B':
        cnt-=1
        ans+=l-cnt-i-1
print(ans)