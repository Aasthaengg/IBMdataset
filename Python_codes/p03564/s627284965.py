n = int(input())
k = int(input())
ans = 1
for _ in range(n):
    dn, dk = ans, k
    ans += min(ans, k)
print(ans)