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
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n+1)]
    for i in range(len(s)):
        pt[s[i]].append(t[i])
        if directed==False:
            pt[t[i]].append(s[i])
    return pt

N = I()
a,b = Line(N-1,2)
c = III()

if N==1:
    print(c[0])
    print(c[0])
    exit()

c.sort()
M = sum(c[:-1])

pt = edges_to_pt(a,b,N)

used = [False]*(N+1)
ans = [0]*(N+1)
used[1] = True
ans[1] = c.pop()
q = [1]
while q:
    q1 = []
    for i in q:
        for j in pt[i]:
            if used[j]==False:
                used[j] = True
                ans[j] = c.pop()
                q1.append(j)
    q = q1

print(M)
print(*ans[1:])