N = int(input())
P = list(map(int, input().split()))

ans = 0
min_n = P[0]
for i in range(N):
    if P[i] <= min_n:
        ans += 1
    min_n = min(min_n, P[i])

print(ans)
