x = int(input())
ans = 0
if x <= 6:
    ans = 1
elif 6 < x < 11:
    ans = 2
else:
    if x % 11 > 6:
        ans = ((x // 11) * 2) + 2
    elif 0 < x % 11 <= 6:
        ans = ((x // 11) * 2) + 1
    elif x % 11 == 0:
        ans = (x // 11) * 2
print(ans)