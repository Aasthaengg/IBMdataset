import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
 
s = input()
ans = math.inf
for x in s:
    t = s.split(x)
    tmp = 0
    for i in range(len(t)):
        tmp = max(tmp, len(t[i]))
    ans = min(ans, tmp)
print(ans)