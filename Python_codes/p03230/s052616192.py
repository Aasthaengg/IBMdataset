import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def a(i):
    return i*(i+1)//2

def main():
    n = I()
    k = -1
    for i in range(1, 10**3):
        if n == a(i):
            k = i
            break
    if k == -1:
        print("No")
        return

    print("Yes")

    print(2 * n // k)
    ans = [[] for __ in range(2 * n // k)]
    for i in range(k):
        ans[0].append(i+1)
    filled = 1
    next_to_use = [1]
    cur_max = k
    for i in range(k-1):
        remain = k
        for j in range(len(next_to_use)):
            ans[i+1].append(next_to_use[j])
            next_to_use[j] += 1
            remain -= 1
        first = True
        while remain:
            cur_max += 1
            ans[i+1].append(cur_max)
            remain -= 1
            if first:
                next_to_use.append(cur_max)
                first = False
    for i in range(k):
        ans[-1].append(ans[i][-1])

    for i in range(len(ans)):
        l = len(ans[i])
        print(str(l) + ' ' + ' '.join([str(x) for x in ans[i]]))
main()

