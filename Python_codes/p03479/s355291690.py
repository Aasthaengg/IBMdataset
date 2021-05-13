X,Y = map(int, input().split())


def sol(x,y):
    count = 1
    start = x
    while True:
        start += start
        if start >y:
            break
        count +=1
    print(count)

sol(X,Y)
