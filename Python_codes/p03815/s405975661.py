x = int(input())

ans = (x // 11) * 2
c = x % 11
if c == 0:
    print(ans)
elif c <= 6:
    print(ans + 1)
else:
    print(ans + 2)