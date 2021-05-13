n = int(input())
a = list(map(int, input().split()))

l = [0]*9
for i in a:
    if 1<=i<=399:
        l[0] = 1
    elif 400<=i<=799:
        l[1] = 1
    elif 800<=i<=1199:
        l[2] = 1
    elif 1200<=i<=1599:
        l[3] = 1
    elif 1600<=i<=1999:
        l[4] = 1
    elif 2000<=i<=2399:
        l[5] = 1
    elif 2400<=i<=2799:
        l[6] = 1
    elif 2800<=i<=3199:
        l[7] = 1
    else:
        l[8] += 1
ls = l[:8]

if sum(ls) == 0:
    print(1, l[8])
else:
    print(sum(ls), sum(l))