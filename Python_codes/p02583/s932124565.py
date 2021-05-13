from itertools import combinations 

N=input()
L=[int(x) for x in input().split()]
comb = combinations(L, 3)
c = 0
for x in comb:
    t=list(x)
    t.sort()
    if t[0]!=t[1] and t[1]!=t[2] and t[0]!=t[2] and t[0]+t[1]>t[2]:
        c += 1
print(c)