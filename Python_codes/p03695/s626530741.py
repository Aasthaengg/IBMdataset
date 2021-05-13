n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 8
free = 0

for _a in a:
    if 1 <= _a <= 399:
        cnt[0] = 1
    elif 400 <= _a <= 799:
        cnt[1] = 1
    elif 800 <= _a <= 1199:
        cnt[2] = 1
    elif 1200 <= _a <= 1599:
        cnt[3] = 1
    elif 1600 <= _a <= 1999:
        cnt[4] = 1
    elif 2000 <= _a <= 2399:
        cnt[5] = 1
    elif 2400 <= _a <= 2799:
        cnt[6] = 1
    elif 2800 <= _a <= 3199:
        cnt[7] = 1
    else:
        free += 1

if free == n:
    print(1, free)
else:
    print(sum(cnt), sum(cnt) + free)