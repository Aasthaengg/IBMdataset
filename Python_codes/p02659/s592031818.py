from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = list(input().split())

b=0
keta = 2
for i in range(len(n[1])):
    if n[1][i] == '.':
        continue
    b += int(n[1][i]) * 10 ** keta
    keta -= 1

print(int(n[0])*b//100)
