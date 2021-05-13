N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
for i in X:
    print(Y[N//2] if i <= Y[N//2-1] else Y[N//2-1])

