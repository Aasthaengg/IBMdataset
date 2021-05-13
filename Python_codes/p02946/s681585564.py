import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
k, x = M()
ans = list()
for i in range(1, k):
    ans.append(x-i)
ans.append(x)
for i in range(1, k):
    ans.append(x+i)
ans.sort()
print(' '.join(map(str, ans)))