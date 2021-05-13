import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MAX = 10**18
MIN = -10**18
MOD = 998244353


def judge(li):
    c = s[0]
    for i in range(len(li)):
        if li[i] == False:
            c += s[i+1]
        else:
            c += "+" + s[i+1]
    return c
s = input()
n = len(s)-1
ans = 0
for i in range(2**n):
    li = [False]*(n)
    for j in range(n):
        if (i>>j)&1:
            li[n-j-1] = True
    a = judge(li)
    e = a[0]
    sumli = []
    for j in range(1,len(a)):
        if a[j] == "+":
            sumli.append(int(e))
            e = ""
        else:
            e += a[j]
    sumli.append(int(e))
    ans += sum(sumli)
print(ans)