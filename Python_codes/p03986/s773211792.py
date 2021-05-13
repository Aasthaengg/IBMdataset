s=input() ; n=len(s)
ss=n//2; tt=n//2
ans=0
for i in range(n):
    if s[i]=="S":
        ans=max(ans, ss-tt)
        ss-=1
    else:
        tt-=1
print(ans*2)