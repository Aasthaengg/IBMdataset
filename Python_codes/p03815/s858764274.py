x = int(input())

div = x // 11
mod = x % 11

if (mod == 0):
    ans = div * 2

elif (0 < mod <= 6):
    ans = div * 2 + 1
else:
    ans = div * 2 + 2

print(ans)
