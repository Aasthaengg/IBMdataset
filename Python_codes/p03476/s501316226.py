import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

s = set()
for i in range(2, 10**5+5):
    if i in s:
        continue
    cnt = 2
    while i*cnt<=10**5+5:
        s.add(i*cnt)
        cnt += 1

from itertools import accumulate

lis = [0]*(10**5+5)
for i in range(3, 10**5+5, 2):
    if not i in s and not (i+1)//2 in s:
        lis[i] = 1

lis = list(accumulate(lis))
Q = int(input())
for _ in range(Q):
    l, r = mapint()
    print(lis[r]-lis[l-1])