n = int(input())
x = []
y = []
for _ in range(n):
    line = list(map(int, input().split()))
    x.append(line[0])
    y.append(line[1])
if n >= 2:
    slope = []
    for i in range(n):
        for j in range(i+1, n):
            X = x[j] - x[i]
            Y = y[j] - y[i]
            if X != 0:
                if X < 0:
                    X = -X
                    Y = -Y
            slope.append([X, Y])
            if X == 0:
                slope.append([X, -Y])
    cnt = []
    for i in slope:
        cnt.append(slope.count(i))
    print(n - max(cnt))
else:
    print(1)