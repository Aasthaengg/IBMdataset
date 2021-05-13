temp = input().split(" ")
X = int(temp[0])
Y = int(temp[1])
i = 2
while True:
    tgt = X * i
    if X == Y:
        print(-1)
        break
    elif tgt % Y != 0:
        print(tgt)
        break
    elif i == 100000:
        print(-1)
        break
    else:
        i += 1