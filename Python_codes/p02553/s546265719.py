a,b,c,d=map(int,input().split())
ans=0
if a>=0:
    if c>=0:
        ans=b*d
    elif d>=0:
        ans=b*d
    else:
        ans=a*d
elif b>=0:
    if c>=0:
        ans=b*d
    elif d>=0:
        ans=max(b*d,a*c)
    else:
        ans=a*c
else:
    if c>=0:
        ans=b*c
    elif d>=0:
        ans=a*c
    else:
        ans=a*c
print(ans)