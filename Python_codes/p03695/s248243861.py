N = int(input())
data = [0 for _ in range(9)]
a = list(map(int, input().split()))
for i in range(N):
    x = a[i]
    if 0 <= x <= 399:
        data[0] = 1
    elif 400 <= x <= 799:
        data[1] = 1
    elif 800 <= x <= 1199:
        data[2] = 1
    elif 1200 <= x <= 1599:
        data[3] = 1
    elif 1600 <= x <= 1999:
        data[4] = 1
    elif 2000 <= x <= 2399:
        data[5] = 1
    elif 2400 <= x <= 2799:
        data[6] = 1
    elif 2800 <= x <= 3199:
        data[7] = 1
    else:
        data[8] += 1

Sum = 0
for i in range(8):
    if data[i] != 0:
        Sum += 1
m = max(1, Sum)
M = Sum + data[8]

print(m,M)

