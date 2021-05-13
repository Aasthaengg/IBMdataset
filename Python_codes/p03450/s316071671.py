#https://onlinejudge.u-aizu.ac.jp/solutions/problem/DSL_1_B/review/3161450/jakenu0x5e/Python3

import sys
readline = sys.stdin.readline
write = sys.stdout.write

n,m = map(int, readline().split())
*p, = range(n+1)
data = [0]*(n+1)

def root(x):
    if x == p[x]:
        return x
    r = p[x]
    p[x] = y = root(r)
    data[x] += data[r]

    return y
    
def unite(x, y, z):
    px = root(x); py = root(y)
    if px == py:
        return 0
    if px < py:
        p[py] = px
        data[py] = data[x] - data[y] + z
    else:
        p[px] = py
        data[px] = data[y] - data[x] - z
    return 1


ans = []

for i in range(m):
    li,ri,di = map(int, readline().split())
    pl = root(li); pr = root(ri)
    if pl == pr:
        if data[ri] - data[li] != di:
            print("No")
            exit()
    else:
        unite(li,ri,di)
#print(data)        
print("Yes")
