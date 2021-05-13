w,a,b=map(int,input().split())
ans=b
if b>a and a+w<b:
    ans=b-a-w
elif b>a and a+w>b:
    ans=0
elif a>b and b+w<a:
    ans=a-b-w
else:
    ans=0
print(ans)