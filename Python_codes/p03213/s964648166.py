n=int(input())
def fact(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

from collections import defaultdict
d = defaultdict(int)
for i in range(1,n+1):
    for itm in fact(i):
        if itm[0]!=1:
            d[itm[0]]+=itm[1]
keys = d.keys()
a=0
for p in keys:
    if d[p]>=74:
        a+=1
    for q in keys:
        if p==q:
            continue
        if d[p] >=2 and d[q]>=24:
            a+=1
        if d[p] >=4 and d[q]>=14:
            a+=1
        for r in keys:
            if q==r or r==p:
                continue
            if d[p] >=2 and d[q]>=4 and d[r]>=4:
                a+=0.5

print(int(a))