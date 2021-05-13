import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
d = LIST()
m = INT()
t = LIST()
d.sort()
t.sort()
j = 0
for i in range(n):
    if(d[i]==t[j]):
        j += 1
    if(j == m):
        break
if(j == m):
    print("YES")
else:
    print("NO")