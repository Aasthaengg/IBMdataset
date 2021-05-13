x = int(input())
ans = 0
if x % 11 == 0:
    ans = 2 * (x // 11)
elif x % 11 <= 6:
    ans = 2 * (x // 11) + 1
else:
    ans = 2 * (x // 11) + 2
print(ans)