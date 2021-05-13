import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

k,a,b = MAP()
if(b-a<=1):
    ans = 1 + k
else:
    n = (1+k-a)//2
    ans = 1 + k - 2*n + (b-a)*n
print(ans)