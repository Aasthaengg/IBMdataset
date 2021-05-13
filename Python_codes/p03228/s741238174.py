import math
inp = input().split()

a = int(inp[0])
b = int(inp[1])
k = int(inp[2])


def cookie(giver,getter):
    if giver%2 == 0:
        sub = math.floor(giver/2)
        giver = giver - sub
        getter = getter + sub
    else:
        tmp = giver - 1
        sub = math.floor(tmp/2)
        giver = giver - 1 - sub
        getter = getter +  sub


for i in range(k):
    if i%2 == 0:
        if a%2 == 0:
            sub = math.floor(a / 2)
            a = a - sub
            b = b + sub
        else:
            tmp = a - 1
            sub = math.floor(tmp / 2)
            a = a - 1 - sub
            b = b + sub
    else:
        if b%2 == 0:
            sub = math.floor(b/ 2)
            b = b - sub
            a = a + sub
        else:
            tmp = b - 1
            sub = math.floor(tmp / 2)
            b = b - 1 - sub
            a = a + sub


print(a,b)
