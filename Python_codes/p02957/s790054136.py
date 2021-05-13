a, b = map(int,input().split())

flg = False
if (b - a) % 2 == 0:
    flg = True

print((a+b)//2) if flg else print('IMPOSSIBLE')