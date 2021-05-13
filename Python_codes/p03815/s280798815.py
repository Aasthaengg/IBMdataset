x = int(input())

ans = (x // 11) * 2
if 0 < x % 11 < 7:
    ans += 1
elif 6 < x % 11:
    ans += 2

print(ans)