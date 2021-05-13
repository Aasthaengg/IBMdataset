import math

l = [int(input()) for i in range(5)]

time = 0
last = 0
for i in range(5):
    time += math.ceil(l[i] / 10) * 10
    if l[i] % 10 == 0:
        continue
    else:
        last = max(last, 10 - (l[i] % 10))

print(time - last)
