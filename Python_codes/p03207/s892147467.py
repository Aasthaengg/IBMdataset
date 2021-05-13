n = int(input())
a = 0
ans = 0
for i in range(n):
    k = int(input())
    a = max(a, k)
    ans += k

ans -= a // 2

print(ans)