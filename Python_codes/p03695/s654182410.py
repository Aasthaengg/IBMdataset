n = int(input())
A = list(map(int, input().split()))
X = [0]*8
y = 0

for a in A:
    if 1 <= a <= 399:
        X[0] = 1
    elif 400 <= a <= 799:
        X[1] = 1
    elif 800 <= a <= 1199:
        X[2] = 1
    elif 1200 <= a <= 1599:
        X[3] = 1
    elif 1600 <= a <= 1999:
        X[4] = 1
    elif 2000 <= a <= 2399:
        X[5] = 1
    elif 2400 <= a <= 2799:
        X[6] = 1
    elif 2800 <= a <= 3199:
        X[7] = 1
    else:
        y += 1

if sum(X) == 0:
    print(1, y)
else:
    print(sum(X), sum(X)+y)
