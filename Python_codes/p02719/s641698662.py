n, k = map(int, input().split())

r = n % k

ans = min(r, k - r)

print(ans)