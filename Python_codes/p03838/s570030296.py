import sys

x, y = map(int, sys.stdin.readline().strip().split())

ans = 0
if abs(x) == abs(y):
    if x == y:
        print(ans)
    else:
        print(1)
elif abs(x) <= abs(y):
    if x < 0:
        # Bを押して符号を入れ替える
        x *= -1
        ans += 1

    tmp = abs(y) - x
    x += tmp
    if x == y:
        print(ans + tmp)
    else:
        # yが負なのでBを押して符号を入れ替える
        print(ans + tmp + 1)
else:
    if x > 0:
        # Bを押して符号を負にする
        x *= -1
        ans += 1

    tmp = abs(x) - abs(y)
    x += tmp
    if x == y:
        print(ans + tmp)
    else:
        # yが負なのでBを押して符号を入れ替える
        print(ans + tmp + 1)