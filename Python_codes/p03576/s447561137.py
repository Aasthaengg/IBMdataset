#PythonだとTLEする
N, K = map(int, input().split())
X = [0] * N
Y = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    X[i] = x
    Y[i] = y

def count(x_min, x_max, y_min, y_max):
    cnt = 0
    for i in range(N):
        if x_min <= X[i] <= x_max and y_min <= Y[i] <= y_max:
            cnt += 1
    return cnt

ans = 10 ** 20
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                # print ('i, j , k, l = ', i, j, k, l)
                if X[i] < X[j] and Y[k] < Y[l]:
                    if count(X[i], X[j], Y[k], Y[l]) >= K:
                        # print ('A')
                        ans = min(ans, (X[j] - X[i]) * (Y[l] - Y[k]))
print (ans)

