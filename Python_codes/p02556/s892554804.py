N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    x[i]=a+b
    y[i]=a-b
xmax=max(x)
xmin=min(x)
ymax=max(y)
ymin=min(y)
print(max(xmax-xmin,ymax-ymin))
