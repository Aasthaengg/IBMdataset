def func(x, y):
    temp = 0
    for i in range(y-1, x/2, -1):
        if x-i > 0:
            temp += 1
    return temp

while(1):
    ans = 0
    n, x = map(int, raw_input().split())
    if n == 0 and x == 0:
        break
    else:
        for i in range(n, 0, -1):
            if x-i < 3:
                ans = 0
            else:
                ans += func(x-i, i)
    print ans