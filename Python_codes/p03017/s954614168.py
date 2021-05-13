n, a, b, c, d = map(int, input().split())
s = input()
if c < d:
    flg = False
    for i in range(a - 1, c):
        if s[i] == "#":
            if flg:
                print("No")
                exit()
            flg = True
        else:
            flg = False
    for i in range(b - 1, d):
        if s[i] == "#":
            if flg:
                print("No")
                exit()
            flg = True
        else:
            flg = False
    print("Yes")

else:
    flg = False
    for i in range(a - 1, c):
        if s[i] == "#":
            if flg:
                print("No")
                exit()
            flg = True
        else:
            flg = False
    flg = 0
    for i in range(b - 2, d + 1):
        if s[i] == ".":
            if flg == 2:
                print("Yes")
                exit()
            flg += 1
        else:
            flg = 0
    print("No")
