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

N = I()

d = defaultdict(int)
for i in range(2,10**5):
    if i*(i-1)//2 > 10**5:
        break
    d[i*(i-1)//2] = i

if d[N]==0:
    print('No')
    exit()

k = d[N]
group = [[] for _ in range(k)]
val = 1
now = 0
while val<=N:
    for i in range(val,N+1):
        if len(group[now])==k-1:
            break
        else:
            group[now].append(i)
    for i in range(now+1,k):
        group[i].append(val)
        val += 1
    now += 1

print('Yes')
print(k)
for i in range(k):
    print(k-1,*group[i])