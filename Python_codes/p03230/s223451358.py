import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())

for i in range(1,1000):
    if i*(i-1)//2 == N:
        k = i
        print('Yes')
        break
    if i == 999:
        print('No')
        exit()

print(k)
ans = [[] for i in range(k)]

now = 1

import itertools
L = [i for i in range(k)]
for v in itertools.combinations(L,2):
    ans[v[0]].append(now)
    ans[v[1]].append(now)
    now += 1
for aaa in ans:
    print(len(aaa),' '.join(map(str,aaa)))
