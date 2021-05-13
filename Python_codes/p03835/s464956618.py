K, S = [int(x) for x in input().split()]

ans = 0

for x in range(max(0, S - 2 * K), min(K, S) + 1):
    ans += min(K, S - x) - max(0, S - x - K) + 1

print(ans)