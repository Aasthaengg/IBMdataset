x = int(input())

k = 1
angle = x

while True:
    if angle >= 360 and angle % 360 == 0:
        break
    angle += x
    k += 1

print(k)
