from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

x = ii()

for a in range(-200,200,1):
    for b in range(-200,200,1):
        if a**5 - b**5 == x:
            print(a,b)
            exit()
