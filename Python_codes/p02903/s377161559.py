import sys
from collections import Counter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h,w,a,b=mp()
for i in range(b):
    print("1"*a+"0"*(w-a))
for i in range(h-b):
    print("0"*a+"1"*(w-a))