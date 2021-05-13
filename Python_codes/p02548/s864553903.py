def readInt():
    return int(input())
def readList():
    return list(map(int,input().split()))
def readMap():
	return map(int,input().split())
def readStr():
    return input()
inf=float('inf')
mod = 10**9+7
import math
from itertools import permutations
def solve(N):
    count=0
    for i in range(1,N):
        count+=(N-1)//i
    return count

N=readInt()
print(solve(N))