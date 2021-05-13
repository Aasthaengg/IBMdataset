a,b,c=map(int,input().split())
res=False
for i in range(b-1):
    if (i*a-c)%b==0:
        res=True
        break

if res:
    print("YES")
else:
    print("NO")
