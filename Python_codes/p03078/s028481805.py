x,y,z,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
b = sorted(list(map(int,input().split())),reverse=True)
c = sorted(list(map(int,input().split())),reverse=True)

buf = []
for i in range(x):
    for j in range(y):
        buf.append(a[i]+b[j])

buf = sorted(buf,reverse=True)[:k]
ans = []

for i in buf:
    for j in range(z):
        ans.append(i+c[j])

ans = sorted(ans,reverse=True)
[print(ans[i]) for i in range(k)]
