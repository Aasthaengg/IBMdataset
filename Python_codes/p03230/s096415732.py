import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

import itertools

n = ni()
k = -1

for i in range(1,10**7):
    if i*(i-1)//2 > n:
        break
    elif i*(i-1)//2 == n:
        k = i

if k == -1:
    print('No')
    exit()

print('Yes')
print(k)

a = list(itertools.combinations(range(k), 2))
ans = [[] for i in range(k)]

for i in range(len(a)):
    x,y = a[i]
    ans[x].append(i+1)
    ans[y].append(i+1)

for l in ans:
    print(str(k-1) + ' ' + (' '.join([str(u) for u in l])))
