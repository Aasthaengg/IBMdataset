N = int(input())
X = list(map(int,input().split()))
Y = sorted(X[:])
Y1 = Y[N//2-1]
Y2 = Y[N//2]
for i in range(N):
    if X[i]>Y1:
        print(Y1)
    else:
        print(Y2)