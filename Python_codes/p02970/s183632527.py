import sys
input = sys.stdin.readline
import math
import collections
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

n,d=MI()
ans=math.ceil(n/(2*d+1))
print(ans)