import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Xs = list(mapint())
cX = Xs[:]
cX.sort()

lm = cX[N//2-1]
rm = cX[N//2]

for x in Xs:
    if x<=lm:
        print(rm)
    else:
        print(lm)