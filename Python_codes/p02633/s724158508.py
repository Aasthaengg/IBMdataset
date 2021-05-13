x = int(input())

k = 1
while True:
    if x*k % 360 == 0:
        print(k)
        exit()
    k += 1