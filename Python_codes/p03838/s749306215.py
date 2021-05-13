def answer(x, y):
    absX = abs(x)
    absY = abs(y)
    a = abs(absY - absX)
    # 0인 경우는 좀 다르게 취급된다
    if x == 0:
        if y > 0:
            return y
        else:
            return -y+1
    if y == 0:
        if x > 0:
            return 1+x
        else:
            return -x
        
    # 둘다 양수
    if (x > 0 and y > 0):
        if absX < absY:
            return y-x
        else:
            return 1+(x-y)+1
    if (x < 0 and y > 0):
        if absX < absY:
            return 1+(y+x)
        else:
            return -(x+y)+1
    if (x > 0 and y < 0):
        if absX < absY:
            return -(y+x)+1
        else:
            return 1+(x+y)
    if (x < 0 and y < 0):
        if absX < absY:
            return 1+(x-y)+1
        else:
            return y-x

x, y = map(int, input().split())
print(answer(x, y))