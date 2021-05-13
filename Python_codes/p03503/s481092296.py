import sys
input = sys.stdin.readline
from itertools import combinations

def readlines(n):
    for _ in range(n):
        yield list(map(int,input().split()))

def bene(me, f, p):
    a = len([0 for m in me if f[m] == 1])
    return p[a]

def main():
    n = int(input())
    F = list(readlines(n))
    P = list(readlines(n))

    for i in range(1, 11):
        for comb in combinations(range(10), i):
            yield sum(bene(comb, f, p) for f, p in zip(F,P))

    
print(max(main()))