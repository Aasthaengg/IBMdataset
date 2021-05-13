import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
T, A = mapint()
Hs = list(mapint())
ths = [(abs(A-(T-(x*0.006))), i+1) for i, x in enumerate(Hs)]
ths.sort()

print(ths[0][1])