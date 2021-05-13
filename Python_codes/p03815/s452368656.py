x = int(input())

ans = (x // 11) * 2
tmp = x % 11

if tmp <= 6 and tmp != 0:
    ans += 1
elif tmp == 0:
    pass
else:
    ans += 2

print(ans)
