import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Vs = list(mapint())
Vs.sort()
val = Vs[0]
for v in Vs[1:]:
    val = (val+v)/2

print(val)