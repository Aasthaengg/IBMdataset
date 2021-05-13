#a,b,x=map(int,input().split())

n=int(input())
s=[input() for i in range(n)]

ans=0
ab=0
xa=0
bx=0
for i in range(n):
    ans+=s[i].count('AB')

    if s[i][-1]=='A' and s[i][0]=='B':
        ab+=1
    elif s[i][-1]=='A':
        xa+=1
    elif s[i][0]=='B':
        bx+=1

cnt=min(ab+xa,ab+bx) if (xa!=0 or bx!=0) else ab-1
print(ans+cnt if cnt>0 else ans)