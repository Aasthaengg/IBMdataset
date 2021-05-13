n=int(input())
xa=0
bx=0
ba=0
ans=0
for i in range(n):
    l=list(input())
    for j in range(len(l)-1):
        if l[j]=='A' and l[j+1]=='B':
            ans += 1
    if l[0]=='B':
        if l[len(l)-1]=='A':
            ba += 1
        else:
            bx += 1
    elif l[len(l)-1]=='A':
        xa += 1
if ba>0:
    ans += ba-1
    if xa>0:
        ans += 1
        xa -= 1
    if bx>0:
        ans += 1
        bx -= 1
ans += min(xa,bx)
print(ans)