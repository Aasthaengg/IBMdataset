K,S = map(int, input().split())

X_m = max(0, S - 2*K)
X_M = min(K, S)

ans = 0

for i in range(X_m, X_M+1):
    Y_m = max(0, S - i - K)
    Y_M = min(K, S - i)
    ans += Y_M - Y_m + 1

print(ans)