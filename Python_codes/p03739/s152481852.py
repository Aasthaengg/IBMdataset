from itertools import accumulate
n = int(input())
a = list(map(int,input().split()))
p = list(accumulate(a))
plan = 0
cou = 0
for i in range(n):
    if i % 2 == 0:
        if p[i] + cou > 0:
            continue
        elif p[i] + cou <= 0:
            plan += abs(p[i]+cou) + 1
            cou = 1-p[i]
    elif i % 2 == 1:
        if p[i] + cou < 0:
            continue
        elif p[i] + cou >= 0:
            plan += p[i] + cou + 1
            cou = -1-p[i]
mian = 0
cou = 0
for i in range(n):
    if i % 2 == 1:
        if p[i] + cou > 0:
            continue
        elif p[i] + cou <= 0:
            mian += abs(p[i]+cou) + 1
            cou = 1-p[i]
    elif i % 2 == 0:
        if p[i] + cou < 0:
            continue
        elif p[i] + cou >= 0:
            mian += p[i] + cou + 1
            cou = -1-p[i]
print(min(mian,plan))