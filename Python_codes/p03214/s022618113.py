import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

median = sum(As)/N
lis = [(abs(a-median), i) for i, a in enumerate(As)]
lis.sort()
print(lis[0][1])
