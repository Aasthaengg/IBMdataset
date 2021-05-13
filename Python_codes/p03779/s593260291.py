import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

x = INT()
i = 1
while(x-i>0):
    x -= i
    i += 1
print(i)