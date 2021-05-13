import math

N = int(input())

fl = math.floor(N / 1.08)
cl = math.ceil(N / 1.08)

if math.floor(fl * 1.08) == N:
    print(fl)
elif math.floor(cl * 1.08) == N:
    print(cl)
else:
    print(":(")