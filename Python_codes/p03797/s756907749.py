n, m = map(int, input().split())
ans = min(n, m//2)
n -= ans
m -= (ans * 2)
ans += (m // 4)
print(ans)