time = [int(input()) for _ in range(5)]

amari = [10]
for i in range(5):
    if time[i]%10 != 0:
        amari += [time[i]%10]
mia = min(amari)


import math
ti = 0
for i in range(5):
    ti += math.ceil(time[i]/10)*10


print(ti-10+mia)