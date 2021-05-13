x = int(input())

q = x // 11
r = x % 11
if r == 0:
    ans = q * 2
elif r < 7:
    ans = q * 2 + 1
else:
    ans = q * 2 + 2
print(ans)
