import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
h = LIST()
ans = 0
tmp = 0
for i in range(n):
    for j in range(n):
        if tmp < h[i]:
            ans += h[i] - tmp
        tmp = h [i]
print(ans)
