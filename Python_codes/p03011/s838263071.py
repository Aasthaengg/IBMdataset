import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))
a,b,c=inp()
print(a+b+c-max(max(a,b),c))
