import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
Bs = list(mapint())

ap = 0
bp = 0
for a, b in zip(As, Bs):
    if a>b:
        ap += a-b
    else:
        bp += (b-a)//2
if ap>bp:
    print('No')
else:
    print('Yes')