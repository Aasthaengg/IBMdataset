for i in range(1, 10000):
    x, y = map(int, input().split())
    if(x == 0 and y == 0): break
    if(x < y): print(str(x) + " " + str(y))
    else: print(str(y) + " " + str(x))