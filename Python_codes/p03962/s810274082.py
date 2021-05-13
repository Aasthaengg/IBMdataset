a,b,c=map(int,input().split())
ans=3
if a==b:
    ans-=1
    if b==c:
        ans-=1
elif a==c:
    ans-=1
    if b==a:
        ans-=1
elif c==b:
    ans-=1
    if a==c:
        ans-=1
print(ans)       
