n = int(input())
A = list(map(int, input().split()))

X = [0]
for i in range(n):
    if i % 2 == 0:
        X.append(1)
    else:
        X.append(-1)

Y = [-x for x in X]

x = 0
AX = [0] + A
for i in range(1, n + 1):
    temporary = AX[i - 1] + AX[i]
    if temporary * X[i] > 0:
        AX[i] = temporary
    else:
        x += abs(temporary - X[i])
        AX[i] = X[i]

y = 0
AY = [0] + A
for i in range(1, n + 1):
    temporary = AY[i - 1] + AY[i]
    if temporary * Y[i] > 0:
        AY[i] = temporary
    else:
        y += abs(temporary - Y[i])
        AY[i] = Y[i]

print(min(x, y))
