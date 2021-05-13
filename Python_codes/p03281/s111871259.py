import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
cnt = 0
for i in range(1, n+1, 2):
    divcnt = 0
    for j in range(1, i+1, 2):
        if i % j == 0:
            divcnt += 1
    if divcnt == 8:
        cnt += 1
print(cnt)