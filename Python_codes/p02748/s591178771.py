a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = [list(map(int,input().split())) for i in range(m)]
x,y,c = [list(i) for i in zip(*l)]
p = min(a) + min(b)

for i in range(m):
    p = min(p,a[x[i]-1] + b[y[i]-1] - c[i])

print(p)