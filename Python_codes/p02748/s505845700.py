A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
y=[]
c=[]
for _ in range(M):
    x0,y0,c0=map(int,input().split())
    x.append(x0)
    y.append(y0)
    c.append(c0)

ans = min(a) + min(b)

for i in range(M):
    price = a[x[i]-1] + b[y[i]-1] - c[i]
    if price < ans:
        ans = price

print(ans)
