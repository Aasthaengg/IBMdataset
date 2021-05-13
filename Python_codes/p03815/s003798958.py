x = int(input())

cnt = x // 11
if cnt * 11 == x:
    print(cnt * 2)
elif cnt * 11 + 6 >= x:
    print(cnt * 2 + 1)
else:
    print(cnt * 2 + 2)
