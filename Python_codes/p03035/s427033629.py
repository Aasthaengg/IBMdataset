import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

a,b=inp()
if a>=13:print(b)
elif a<=5:print(0)
else:print(b//2)