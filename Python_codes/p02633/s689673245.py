X = int(input())

for i in range(1, 1000000):
    if (X * i) % 360 == 0:
        print(i)
        exit()
