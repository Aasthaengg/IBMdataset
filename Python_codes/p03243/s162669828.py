n = int(input())
for x in range(111, 1000, 111):
    if x >= n:
        print(x)
        exit()