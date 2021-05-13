K, X = map(int,input().split())

X_min = X - K + 1
X_max = X + K

print(*list(range(X_min,X_max)))