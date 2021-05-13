import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()
ans = 'Yes'
for i in range(len(s)):
    if i%2 == 0:
        if s[i] == 'L':
            ans = 'No'
    else:
        if s[i] == 'R':
            ans = 'No'
print(ans)