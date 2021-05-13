import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
from collections import Counter
c = Counter(S)
if abs(c['a']-c['b'])<=1 and abs(c['a']-c['c'])<=1 and abs(c['b']-c['c'])<=1:
    print('YES')
else:
    print('NO')