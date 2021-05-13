W, a, b = map(int, input().split())

if a<=b :
    if a+W<b : print(b - a - W)
    else : print(0)
else :
    if b+W < a : print(a - b - W)
    else : print(0)
