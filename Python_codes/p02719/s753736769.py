n, k = map(int, input().split())
n %= k
ans = min(n, k - n)
print(ans)