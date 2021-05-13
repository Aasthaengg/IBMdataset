import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# ソートして上位A個を使うと最大
# 場合の数は，vの最大値がA個以上あるかで場合分け

N,A,B = LI()
v = LI()

def linear_nCk(n,k):
    a = [1]*(k+1)
    for i in range(1,k+1):
        a[i] = a[i-1]*(n-k+i)//i
    return a[-1]

v.sort(reverse=True)

d = defaultdict(int)
use = defaultdict(int)

for i in range(N):
    d[v[i]] += 1
    if i < A:
        use[v[i]] += 1

if v[0] == v[A-1]:
    num = d[v[0]]
    ans = 0
    for i in range(A,min(B+1,num+1)):
        ans += linear_nCk(num,i)
    print(v[0])
    print(ans)
else:
    max_val = 0
    ans = 1
    for k,v in use.items():
        ans *= linear_nCk(d[k],v)
        max_val += k*v
    print(max_val/A)
    print(ans)