n = int(input())
a = list(map(int, input().split()))

count = [0] * 9
for i in a:
    if 1 <= i <= 399:
        count[0] = 1
    elif 400 <= i <= 799:
        count[1] = 1
    elif 800 <= i <= 1199:
        count[2] = 1
    elif 1200 <= i <= 1599:
        count[3] = 1
    elif 1600 <= i <= 1999:
        count[4] = 1
    elif 2000 <= i <= 2399:
        count[5] = 1
    elif 2400 <= i <= 2799:
        count[6] = 1
    elif 2800 <= i <= 3199:
        count[7] = 1
    else:
        count[8] += 1

mx = sum(count[:8]) + count[8]
mn = 0
if sum(count[:8]) == 0 and count[8] != 0:
    mn = 1
else:
    mn = sum(count[:8])

print(mn, mx)