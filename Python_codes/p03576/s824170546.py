n, kosuu = map(int, input().split())
XY, X, Y = [], [], []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    XY.append([x,y])

X = sorted(X, reverse=True)
Y = sorted(Y, reverse=True)

s_min = 10**20
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                count = 0
                x_max = X[i]
                x_min = X[-1*(j+1)]
                if x_max <= x_min:
                    continue
                y_max = Y[k]
                y_min = Y[-1*(l+1)]
                if y_max <= y_min:
                    continue

                s = abs(x_max-x_min)*abs(y_max-y_min)

                for m in range(n):
                    x = XY[m][0]
                    y = XY[m][1]
                    if (x <= x_max and x >= x_min) and (y <= y_max and y >= y_min):
                        count += 1
                if count >= kosuu:
                    s_min = min(s, s_min)

print(s_min)

