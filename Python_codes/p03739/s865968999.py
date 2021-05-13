n = int(input())
a = list(map(int, input().split()))
t = 1
cand1 = 0
tmp = 0
for ai in a:
    if (tmp + ai) * t <= 0:
        cand1 += abs(tmp + ai - t)
        tmp = t
    else:
        tmp += ai
    t *= -1
t = -1
cand2 = 0
tmp = 0
for ai in a:
    if (tmp + ai) * t <= 0:
        cand2 += abs(tmp + ai - t)
        tmp = t
    else:
        tmp += ai
    t *= -1

print(min(cand1, cand2))