n,a,b=map(int,input().split())
x=list(map(int,input().split()))
y=[]
for i in range(n-1):
    y.append(a*(x[i+1]-x[i]))
ans=0
for i in y:
    if i<=b:
        ans+=i
    else:
        ans+=b

print(ans)