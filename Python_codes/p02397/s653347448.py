flag = "go"
while flag == "go":
    x, y = map(int, input().split())
    if x == y == 0:
        flag = "stop"
    else:
        if x < y:
            print(x,y)
        else:
            print(y,x)
