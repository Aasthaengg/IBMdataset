import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
from collections import Counter
count = Counter(S)

a = count['a']
b = count['b']
c = count['c']
N = len(S)

N = N//3
if N<=a<=N+1 and N<=b<=N+1 and N<=c<=N+1:
    print('YES')
else:
    print('NO')