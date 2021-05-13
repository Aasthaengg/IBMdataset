n = int(input())

import math
def factorize(n):
    d = {}
    temp = int(math.sqrt(n))+1
    for i in range(2, temp):
        while n%i== 0:
            n //= i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    if d == {}:
        d[n] = 1
    else:
        if n in d:
            d[n] += 1
        elif n != 1:
            d[n] =1
    return d

D = {}
for i in range(1, n+1):
    d = factorize(i)
    for k, v in d.items():
        if k in D:
            D[k] += v
        else:
            D[k] = v
#print(D)
p74 = 0
p24 = 0
p14 = 0
p4 = 0
p2 = 0
for k, v in D.items():
    if v >= 74:
        p74 += 1
        p24 += 1
        p14 += 1
        p4 +=1
        p2 +=1
    elif v >= 24:
        p24 += 1
        p14 += 1
        p4 +=1
        p2 +=1
    elif v >= 14:
        p14 += 1
        p4 +=1
        p2 +=1
    elif v >= 4:
        p4 +=1
        p2 +=1
    elif v >= 2:
        p2 +=1
    else:
        pass

ans = 0
# 3*5*5
ans += (p4*(p4-1)//2)*(p2-2)
# 3*25
ans += p24*(p2-1)
# 5*15
ans += p14*(p4-1)
# 75
ans += p74
print(ans)
