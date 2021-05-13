a,b,c = map(int, input().split())
if a%2 == 1 or b%2 == 1 or c%2 == 1:
    print(0)
    exit()
if a == b == c: 
    print(-1)
    exit()
else:
    count = 0
    while True:
        if a%2 == 1 or b%2 == 1 or c%2 == 1:
            print(count)
            exit()
        else:
            count += 1
            x = (b+c)//2
            y = (c+a)//2
            z = (a+b)//2
            a = x
            b = y
            c = z
