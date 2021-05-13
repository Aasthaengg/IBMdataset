N, K = map(int, input().split())
L = list(map(int, input().split()))
ans = 0

L = sorted(L, reverse=True)

for i in range(0, K, 1):
    ans += L[i]

print(ans)