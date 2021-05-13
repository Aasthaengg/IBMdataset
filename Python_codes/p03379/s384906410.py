N = int(input())
X = [int(x) for x in input().split()]

Y = sorted(X)
for i in range(N):
    if X[i] < Y[N // 2]:
        print(Y[N // 2])
    else:
        print(Y[N // 2 - 1])