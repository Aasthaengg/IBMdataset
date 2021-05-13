# for i, a in enumerate(iterable)
# q, mod = divmod(a, b)
# divmod(x, y) returns the tuple (x//y, x%y)
# manage median(s) using two heapq https://atcoder.jp/contests/abc127/tasks/abc127_f
# visual studio code shortcut https://qiita.com/TakahiRoyte/items/cdab6fca64da386a690b
# delete line: Ctrl+Shift+k
# choose same words: Ctrl+Shift+l
import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7

from itertools import combinations, permutations # https://docs.python.org/ja/3/library/itertools.html
from math import factorial
def combinations_count(n, r):
    # faster than the following code
    # def combinations_count(n, r):
    #     return factorial(n) // (factorial(n - r) * factorial(r))
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result
def combination_with_repetition_count(n, r):
    return combinations_count(n + r - 1, r)
from collections import deque, Counter # https://docs.python.org/ja/3/library/collections.html#collections.deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace,nlargest,nsmallest # https://docs.python.org/ja/3/library/heapq.html
from copy import deepcopy, copy # https://docs.python.org/ja/3/library/copy.html
from functools import reduce
from fractions import gcd # Deprecated since version 3.5: Use math.gcd() instead.
def gcds(numbers):
    return reduce(gcd, numbers)
def lcm(x, y):
    return (x * y) // gcd(x, y)
def lcms(numbers):
    return reduce(lcm, numbers, 1)
# set the inputs
    # open(0).read() is a convenient method:
    # ex) n, m, *x = map(int, open(0).read().split())
    #     min(x[::2]) - max(x[1::2])
    # ex2) *x, = map(int, open(0).read().split())
    #     don't forget to add comma after *x if only one variable is used
    # R = lambda: map(int, input().split()) :it's fashionable, isn't it?
    # ex1) n, k = R()
    # ex2) v = list(R())
    # ex3) bc = [list(R()) for i in range(m)]

# n = 3
# ab = [[1, 3],[2, 3]]
# c = [1, 2, 3]
# c.sort(reverse=True)

R = lambda: list(map(int, input().split()))
input2 = sys.stdin.readline
R2 = lambda: list(map(int, input2().split()))

n = int(input())
ab = [R2() for i in range(n-1)]
c = R2()
c.sort(reverse=True)

# calculate
dic = {}
l = deque()
for a, b in ab:
    dic.setdefault(a, []).append(b)
    dic.setdefault(b, []).append(a)

m = sum(c) - max(c)
d = [-1] * n
l.extend(dic[1])
d[0] = c[0]
i = 1
while l:
    deq = l.popleft()
    if d[deq-1] >= 0:
        pass
    else:
        if deq in dic:
            l.extend(dic[deq])
        d[deq-1] = c[i]
        i += 1
print(m)
print(*d)

