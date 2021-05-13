x = int(input())
ans = x//11 * 2
if x % 11 == 0:
    ans = ans
elif x % 11 > 6:
    ans += 2
else:
    ans += 1
print(ans)
