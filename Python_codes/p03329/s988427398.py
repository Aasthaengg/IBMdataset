n=int(input())
ans=n
for i in range(n+1):
    c=0
    t=i
    while(t>0):
        c+=(t%6)
        t=(t//6)
    t=n-i
    while(t>0):
        c+=(t%9)
        t=(t//9)
    if ans>c:
        ans=c
print(ans)