import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N = I()
A = III()

d = defaultdict(list)
for i in range(N):
    A[i] = format(A[i],'b').zfill(20)
    for j,k in enumerate(A[i]):
        if k=='1':
            d[i].append(j)

used = [False]*20
l = 0
r = 0
ans = 0
for j in d[0]:
    used[j] = True

while l<=N-1:
    ans += r-l+1
    for i in range(r+1,N):
        if all([used[j]==False for j in d[i]]):
            for j in d[i]:
                used[j] = True
            r += 1
            ans += 1
        else:
            break
    for j in d[l]:
        used[j] = False
    l += 1
    if l>r:
        r = l
        for j in d[l]:
            used[j] = True
    
print(ans)