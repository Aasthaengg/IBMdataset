from functools import lru_cache

n = int(input())
A = [int(n) for n in input().split()]
q = int(input())
M = [int(n) for n in input().split()]


@lru_cache(maxsize=2**12)
def makeCombination(i,key):
    if key == 0:
        return True
    if i == n:
        return False
    return makeCombination(i+1,key) or makeCombination(i+1,key-A[i])


for m in M:
    if makeCombination(0,m):
        print("yes")
    else:
        print("no")

