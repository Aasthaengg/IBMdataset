import sys
import math
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()
l,r,d=get_ints()
count=0
for i in range(l,r+1):
    if i%d==0:
        count=count+1
print(count)