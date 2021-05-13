a,b=map(int,input().split())
ans=max(a,b)
if ans==a:
    a=a-1
else:
    b=b-1
ans+=max(a,b)
print(ans)

