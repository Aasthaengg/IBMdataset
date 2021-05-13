a, b, c = map(int, input().split())

ans = 0

# まずは毒入りクッキーを食べきる
eat = min(b, c)
b -= eat
c -= eat
ans += 2 * eat

# 残った枚数に応じて食べ方が違う
if b == 0:
    if a >= c - 1:
        ans += c
    else:
        ans += a+1
else:
    ans += b

print(ans)
