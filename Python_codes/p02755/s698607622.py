from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b = mi()

for i in range(1,1010,1):
    if math.floor(i*0.08) == a and math.floor(i*0.10) == b:
        print(i)
        exit()
print(-1)
