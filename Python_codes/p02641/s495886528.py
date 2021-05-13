x, n = map(int, input().split())
p = list(map(int, input().split()))

if n == 0:
    print(x)
    exit()


Flag = True
i = 0
while Flag:
    if (x - i) not in p:
        print(x - i)
        break
    elif (x + i) not in p:
        print(x + i)
        break
    i += 1
