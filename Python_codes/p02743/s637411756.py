a, b, c = map(int, input().split())
flag = 1

if c - a - b <= 0:
    flag = 0
else:
    L = 4 * a * b
    R = (c - a - b) ** 2
    if L >= R:
        flag = 0

if flag:
    print("Yes")
else:
    print("No")