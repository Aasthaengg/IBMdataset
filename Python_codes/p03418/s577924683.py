# editrialを参考にした
N, K = map(int, input().split())
ans = 0
for b in range(1, N + 1):
    div, mod = divmod(N, b)
    ans += div * max(0, b - K)
    ans += max(mod - K + 1, 0)
if K == 0:
    ans -= N
print(ans)
