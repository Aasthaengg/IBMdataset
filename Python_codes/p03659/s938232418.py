N = int(input())
a = list(map(int, input().split()))
M = sum(a)
S = a[0]
T = M - S
X = abs(T - S)
for i in range(1, N - 1):
    S += a[i]
    T = M - S
    X = min(X, abs(T - S))
print(X)