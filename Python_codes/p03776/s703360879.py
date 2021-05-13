from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = 10**18
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)
def comb(n,r):
    if r > n:
        return 0
    else:
        return factorial(n)//(factorial(n-r)*factorial(r))
n,a,b = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse=True)
max_mean = sum(v[0:a])/a
print(max_mean)
#選び方の総数を求める
c = Counter(v)
i = 0
num = 0
ans = 0
while num<a:
    if num+c[v[i]]>=a:
        num += c[v[i]]
    else:
        num += c[v[i]]
        i += 1
num -= c[v[i]]

if i > 0:
        ans += comb(c[v[i]],a-num)
        print(ans)
else:
    for j in range(a,b+1):
        if c[v[0]] >=j:
            ans += comb(c[v[0]],j)
    print(ans)