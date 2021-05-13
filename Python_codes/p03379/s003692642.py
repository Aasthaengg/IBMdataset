n = int(input())
X = list(map(int, input().split()))
x0, x1 = sorted(X)[n // 2 - 1:n // 2 + 1]
[print(x1) if x <= x0 else print(x0) for x in X]