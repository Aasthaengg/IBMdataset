n=int(input())
s=[input() for _ in range(n)]
c,ca,cb,cab=0,0,0,0
for i in range(n):
    n0=len(s[i])
    if s[i][0]=='B':
        if s[i][n0-1]=='A':cab+=1
        else:cb+=1
    elif s[i][n0-1]=='A':ca+=1
    for j in range(1,n0):
        if s[i][j-1]=='A' and s[i][j]=='B':c+=1
ans=c
if cab>0:
    if ca>0:
        ans+=1
        ca-=1
    ans+=cab-1
    if cb>0:
        ans+=1
        cb-=1
ans+=min(ca,cb)
print(ans)