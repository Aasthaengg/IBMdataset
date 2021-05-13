N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    dist = X[i+1] - X[i]
    if dist * A <= B:
        ans += dist * A
    else:
        ans += B
print(ans)