x = int(input())

while True:
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        print(x)
        exit()
    x += 1

