import math
K = int(input())
A = list(map(int, input().split()))
mincnt = 2
for a in reversed(A):
    if a < mincnt:
        a = math.ceil(mincnt/a) * a
    mincnt = max(mincnt, a)

#print(mincnt)

maxcnt = 2
nowgropu = 1
for a in reversed(A):
    nowgropu = maxcnt // a
    maxcnt = a * (nowgropu + 1) - 1

#print(maxcnt)

def check(init, A):
    cnt = init
    for a in A:
        group = cnt // a
        cnt = group * a
    return cnt == 2

#print(check(mincnt, A))
if check(mincnt, A) and check(maxcnt, A):
    print(mincnt, maxcnt)
else:
    print(-1)

