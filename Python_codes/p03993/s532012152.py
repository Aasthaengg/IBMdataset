import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
a = LI()
ans = 0
for i,x in enumerate(a,1):
    if x=='*':
        continue
    if a[x-1]==i:
        ans += 1
        a[x-1] = '*'
print(ans)
