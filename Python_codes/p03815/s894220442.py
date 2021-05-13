x = int(input())
# 最善手は、6,5,6,5,・・・
q,r = divmod(x, 11)
ans = 2 * q
if 0 < r <= 6:
    ans += 1
elif 6 < r:
    ans += 2

print(ans)