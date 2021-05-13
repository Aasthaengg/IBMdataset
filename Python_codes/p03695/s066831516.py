N = int(input())
A = list(map(int, input().split()))
R = [0] * 8
A.sort()
c = 0
for a in A:
    if 1 <= a < 400:
        R[0] = 1
    elif 400 <= a < 800:
        R[1] = 1
    elif 800 <= a < 1200:
        R[2] = 1
    elif 1200 <= a < 1600:
        R[3] = 1
    elif 1600 <= a < 2000:
        R[4] = 1
    elif 2000 <= a < 2400:
        R[5] = 1
    elif 2400 <= a < 2800:
        R[6] = 1
    elif 2800 <= a < 3200:
        R[7] = 1
    else:
        c += 1

if c != 0 and not 1 in R:
    mi = 1
else:
    mi = R.count(1)
ma = R.count(1) + c

print(mi, ma)