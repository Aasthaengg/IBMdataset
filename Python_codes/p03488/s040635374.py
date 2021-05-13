sl = list(input())
x,y = map(int,input().split())
lrl = [[],[]]
mode = 0
stack = 0
flag = True
first_t = 0
for s in sl:
    if s == "F":
        stack += 1
    else:
        if flag:
            first_t = stack
            flag = False
        elif stack > 0:
            lrl[mode%2].append(stack)
        mode += 1
        stack = 0
else:
    if flag:
        first_t = stack
        flag = False
    elif stack > 0:
        lrl[mode%2].append(stack)

x = abs(x - first_t)
y = abs(y)
from collections import defaultdict
l = defaultdict(int)
r = defaultdict(int)
l[0] = 1
r[0] = 1
ol = x + sum(lrl[0])
for a in lrl[0]:
    kouho = []
    for ll in l:
        if ll + 2 * a <= ol:
            kouho.append(ll+2*a)
    for i in kouho:
        l[i] = 1

orr = y + sum(lrl[1])
for a in lrl[1]:
    kouho = []
    for rr in r:
        if rr + 2 * a <= orr:
            kouho.append(rr+2*a)
    for i in kouho:
        r[i] = 1


if l[ol] == 1 and r[orr] == 1:
    print("Yes")
    import sys
    sys.exit()

print("No")