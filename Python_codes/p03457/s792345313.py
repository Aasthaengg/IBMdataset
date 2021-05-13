N = int(input())
T = []
X = []
Y = []
for _ in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
flag = 0
if T[0]-abs(X[0])-abs(Y[0]) < 0 or (T[0]-abs(X[0])-abs(Y[0]))%2 != 0:
    flag = 1
for i in range(N-1):
    if T[i+1]-T[i]-abs(X[i+1]-X[i])-abs(Y[i+1]-Y[i]) < 0 or (T[i+1]-T[i]-abs(X[i+1]-X[i])-abs(Y[i+1]-Y[i]))%2 != 0:
        flag = 1
print("Yes" if flag == 0 else "No")
