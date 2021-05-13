X = int(input())

k = 0
for i in range(360):
    k += X
    if k % 360 == 0:
        print(i+1)
        break