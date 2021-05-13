from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
x = li()

ave = sum(x) //n

ans1=0
for i in range(n):
    ans1 += (x[i]-ave) ** 2
ans2=0
for i in range(n):
    ans2 += (x[i]-(ave+1)) ** 2
print(min(ans1,ans2))