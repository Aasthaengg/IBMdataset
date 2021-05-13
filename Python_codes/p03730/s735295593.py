from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,c=mi()
for i in range(1,b):
    if (b*i + c) % a == 0:
        print("YES")
        exit()
print("NO")
