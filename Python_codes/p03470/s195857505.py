import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n = I()
li = [I() for _ in range(n)]
li.sort(reverse=True)
before = ans =  0
for i in range(n):
    if before != li[i]:
        ans += 1
        before = li[i]
print(ans)