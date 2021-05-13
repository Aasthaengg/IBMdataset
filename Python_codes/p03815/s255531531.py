x = int(input())
ans = x // 11 * 2
mod = x % 11
if mod != 0:
    if mod > 6:
        ans += 2
    else:
        ans += 1
print(ans)
