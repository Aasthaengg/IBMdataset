x, y = map(int,input().split())

ans = 0
# 正正
if x >= 0 and y >= 0:
    
    if x <= y:
        ans = abs(x-y)
        print(ans)
        exit()
    else:
        if y != 0:
            print(abs(x-y)+2)
        else:
            print(abs(x - y) + 1)

# 正負
if x >= 0 and y < 0:
    if abs(x) >= abs(y):
        x = x * -1
        ans += 1
        ans += abs(x - y)
        print(ans)
        exit()
    else:
        print(abs(y)-x + 1)
# 負正
if y >= 0 and x < 0:
    print(min(abs(x-y), abs(x*-1 - y)+1))

# 負負
if x < 0 and y < 0:
    if x > y:
        print(abs(x - y)+2)
    else:
        print(abs(x-y))
