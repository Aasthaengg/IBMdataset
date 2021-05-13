import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

lis = [0]*N
for a in As:
    lis[a-1]+= 1

for l in lis:
    print(l)