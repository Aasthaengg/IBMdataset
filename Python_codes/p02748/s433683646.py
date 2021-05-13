A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = [0]*M
y = [0]*M
c = [0]*M
for i in range(M):
    x[i],y[i],c[i] = map(int,input().split())

ans = min(a) + min(b)
for i in range(M):
    if a[x[i]-1] + b[y[i]-1] - c[i] < ans:
        ans = a[x[i]-1] + b[y[i]-1] - c[i]
print(ans)