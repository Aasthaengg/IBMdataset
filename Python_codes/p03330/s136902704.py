import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


import sys
def query(i,j):
    print("? {0} {1}".format(i, j))
    sys.stdout.flush()
    return int(input())

n,c = list(map(int, input().split()))
ds = [None]*c
cs = [None]*n
for i in range(c):
    ds[i] = list(map(int, input().split()))
for i in range(n):
    cs[i] = list(map(lambda x : int(x)-1, input().split()))
from itertools import product
ans = float("inf")
v0 = [0]*c
v1 = [0]*c
v2 = [0]*c
for i,j in product(range(n), range(n)):
    if (i+j)%3==0:
        v = v0
    elif (i+j)%3==1:
        v = v1
    else:
        v = v2
    for cc in range(c):
        v[cc] += ds[cs[i][j]][cc]
for c0,c1,c2 in product(range(c), range(c), range(c)):
    if c0==c1 or c0==c2 or c1==c2:
        continue
    val = v0[c0] + v1[c1] + v2[c2]
    ans = min(ans, val)
print(ans)