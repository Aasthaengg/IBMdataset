x = int(input())
ans = x // 11
ans *= 2

m = x % 11
if m >= 7:
    ans += 2
elif m >= 1:
    ans += 1
print(ans)