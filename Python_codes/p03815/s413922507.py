x = int(input())
# 2回で6, 5 -> 11点
i, j = divmod(x, 11)
ans = i * 2
if 0 < j <= 6:
    ans += 1
elif 6 < j:
    ans += 2
print(ans)
