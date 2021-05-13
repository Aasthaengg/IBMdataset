#053_C
x = int(input())

if x % 11 == 0:
    ans = x // 11 * 2
else:
    ans = x // 11 * 2 + (x % 11 > 6) + 1
print(ans)