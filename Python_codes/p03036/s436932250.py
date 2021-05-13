r,D,x = map(int, input().split())
y = []
y.append(x)
for i in range(10):
    print(r*y[i]-D)
    y.append(r*y[i]-D)