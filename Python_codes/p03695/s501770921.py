n = int(input())
a = list(map(int, input().split()))

col = [0] * 8
opt = 0

for i in range(n):
    if 1 <= a[i] < 400:
        col[0] = 1
    elif 400 <= a[i] < 800:
        col[1] = 1
    elif 800 <= a[i] < 1200:
        col[2] = 1
    elif 1200 <= a[i] < 1600:
        col[3] = 1
    elif 1600 <= a[i] < 2000:
        col[4] = 1
    elif 2000 <= a[i] < 2400:
        col[5] = 1
    elif 2400 <= a[i] < 2800:
        col[6] = 1
    elif 2800 <= a[i] < 3200:
        col[7] = 1
    elif 3200 <= a[i]:
        opt += 1
if sum(col) == 0:
    print(1, opt)
else:
    print(sum(col), sum(col)+opt)