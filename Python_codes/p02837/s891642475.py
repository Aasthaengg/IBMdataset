from collections import defaultdict
import itertools

n = int(input())

l = [[] for i in range(n)]
p = [i for i in range(n)]

for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        l[i].append((x,y))

for i in range(n,-1,-1):
    for comb in itertools.combinations(p,i):
        tmp = [1 if j in comb else 0 for j in range(n)]
        F = True
        for c in comb:
            for k in l[c]:
                if tmp[k[0]-1] != k[1]:
                    F = False
        if F:
            print(i)
            exit()

print(0)