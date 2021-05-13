import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

n, m, d = mapint()
l = (min(n, d*2)+max(0, n-2*d)*2)*(m-1) if d!=0 else n*(m-1)
print(l/(n**2))