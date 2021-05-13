x, y = map(int, raw_input().split())
flag = True
while flag:
    if y > x:
        x, y = y, x
    mod = x % y
    x, y = y, mod
    if mod == 0:
        print x
        quit()