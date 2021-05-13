def is_no2(X):
    if X[1] == min(X) or X[1] == max(X):
        return 0
    else:
        return 1

N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    X = [P[i], P[i+1], P[i+2]]
    ans += is_no2(X)

print(ans)