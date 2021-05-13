W, H, N = map(int, input().split())

X = [[i+1, "w"] for i in range(W)]
Y = [[i+1, "w"] for i in range(H)]
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for j in range(len(X)):
            if X[j][0] <= x:
                X[j][1] = "b"
    elif a == 2:
        for j in range(len(X)):
            if X[j][0] > x:
                X[j][1] = "b"
    elif a == 3:
        for j in range(len(Y)):
            if Y[j][0] <= y:
                Y[j][1] = "b"
    elif a == 4:
        for j in range(len(Y)):
            if Y[j][0] > y:
                Y[j][1] = "b"
x_w = 0
y_w = 0
for i in range(len(X)):
    if X[i][1] == "w":
        x_w += 1
for i in range(len(Y)):
    if Y[i][1] == "w":
        y_w += 1
print(x_w * y_w)
