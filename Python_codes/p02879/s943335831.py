from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b=mi()

if a <= 9 and b <= 9:
    print(a*b)
else:
    print(-1)