import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K, T = mapint()
As = list(mapint())
maxi = max(As)
rest = K-maxi
if maxi<=rest+1:
    print(0)
else:
    maxi -= rest+1
    print(maxi)