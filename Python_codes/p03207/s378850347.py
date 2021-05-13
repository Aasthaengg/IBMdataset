N = int(input())
max_price = 0
ans = 0
for i in range(N):
    p = int(input())
    ans += p
    max_price = max(max_price, p)
ans -= max_price // 2
print(ans)