a,b,c = map(int,input().split())

ans=0
if a*b*c%2==0:
    ans=0
else:
    ans = min(a*b,b*c,a*c)
print(ans)