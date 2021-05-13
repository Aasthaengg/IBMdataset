n = int(input())
al = list(map(int, input().split()))

import collections

c = collections.Counter(al)
temp = sorted(list(set(al)),reverse = True)
x = 0
y = 0

for i in temp:
    if c[i]>=4:
        if x ==0:
            x = i
        if y ==0:
            y = i
    elif c[i] >=2:
        if x ==0:
            x =i
        elif y ==0:
            y = i
    if x*y != 0:
        print(x*y)
        exit()    
print(x*y)