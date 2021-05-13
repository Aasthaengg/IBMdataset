n=int(input())
ans=1
p=1
q=1
for i in range(n):
    a,b=map(int,input().split())
    c=a+b
    k=ans//c
    if ans%c!=0:
        k+=1
    l=p//a
    if p%a!=0:
        l+=1
    m=q//b
    if q%b!=0:
        m+=1
    g=max(k,l,m)
    ans=c*g
    p=a*g
    q=b*g
print(ans)
