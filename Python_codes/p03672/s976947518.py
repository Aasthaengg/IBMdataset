import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()
n = len(s)
ans = 0
for i in range(1, n+1):
    temp_s = s[0:n-i]
    temp_n = len(temp_s)
    if temp_s[0:temp_n//2] == temp_s[temp_n//2:]:
        ans = temp_n
        break
print(ans)