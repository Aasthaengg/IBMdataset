x = int(input())
ans = 0
if x % 11 == 0:
    print(2 * (x // 11))
else:
    if x % 11 <= 6:
        print(2 * (x // 11) + 1)
    else:
        print(2 * (x // 11) + 2)