n = int(input())
a = [int(x) for x in input().split()]
d = {}

for i in range(n):
    tmp = a[i]
    if tmp not in d:
        d[tmp] = 0
    d[tmp] += 1

flag1 = False
flag2 = False

for kk in sorted(d.keys(),reverse = True):
    if d[kk] >= 2 and flag1 == False:
        mx_v = kk
        flag1 = True
        d[kk] -= 2
    if flag1 == True and flag2 == False and d[kk] >= 2:
        mn_v = kk
        flag2 = True

if flag1 and flag2:
    print(mx_v * mn_v)
else:
    print(0)
