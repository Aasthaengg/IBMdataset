N = int(input())
lank = [0, 0, 0, 0, 0, 0, 0, 0]
a = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if 1 <= a[i] <= 399:
        lank[0] = 1
    elif 400 <= a[i] <= 799:
        lank[1] = 1
    elif 800 <= a[i] <= 1199:
        lank[2] = 1
    elif 1200 <= a[i] <= 1599:
        lank[3] = 1
    elif 1600 <= a[i] <= 1999:
        lank[4] = 1
    elif 2000 <= a[i] <= 2399:
        lank[5] = 1
    elif 2400 <= a[i] <= 2799:
        lank[6] = 1
    elif 2800 <= a[i] <= 3199:
        lank[7] = 1
    else:
        cnt += 1

number_min = max(1, lank.count(1))
number_max = lank.count(1) + cnt

print(number_min, number_max)