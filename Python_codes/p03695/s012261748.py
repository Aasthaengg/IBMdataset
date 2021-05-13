import sys
import itertools
import copy
from collections import defaultdict

input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

n = I()
mylist = [0 for i in range(8)]
mylist2 = MI()
num = 0

for i in mylist2:
    temp = i // 400
    if temp <= 7:
        mylist[temp] = 1
    else:
        num += 1
        
max = sum(mylist) + num

min = sum(mylist)
if min == 0:
    min = 1
    
print(str(min) + " " + str(max))