from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = list(input())
n = len(s)
d = list('abcdefghijklmnopqrstuvwxyz')
se = set(s)
if n < 26:
    for i,x in enumerate(d):
        if not x in se:
            s.append(x)
            break
    print(''.join(s))
else:
    for i in range(25)[::-1]:
        if s[i] < s[i+1]:
            tmp = s[i+1:n]
            tmp.sort()
            for j in tmp:
                if j > s[i]:
                    s[i] = j
                    break
            # print(i)
            print(''.join(s[:i+1]))
            break
    else:
        print(-1)