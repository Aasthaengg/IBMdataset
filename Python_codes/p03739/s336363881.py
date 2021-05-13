n = int(input())
a = list(map(int,input().split()))

ans1 = 0
ans2 = 0
tmp = 0

for i,e in enumerate(a):
    tmp += e
    if i % 2 == 0:
        if tmp > 0:
            pass
        else:
            ans1 += 1 - tmp
            tmp = 1
    else:
        if tmp < 0:
            pass
        else:
            ans1 += tmp + 1
            tmp = -1

tmp = 0

for i,e in enumerate(a):
    tmp += e
    if i % 2 == 1:
        if tmp > 0:
            pass
        else:
            ans2 += 1 - tmp
            tmp = 1
    else:
        if tmp < 0:
            pass
        else:
            ans2 += tmp + 1
            tmp = -1

print(min(ans1, ans2))
