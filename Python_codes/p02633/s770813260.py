x = int(input())

for i in range(1, 180):
    if 360 * i % x == 0:
        print(360 * i // x)
        break