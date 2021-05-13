a,b=map(int,input().split())
ans=str()
if a<b:
    for i in range(b):
        ans+=str(a)
elif a>b:
    for i in range(a):
        ans+=str(b)
else:
    for i in range(a):
        ans+=str(a)
print(ans)