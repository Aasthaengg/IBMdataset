import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K, X = mapint()
print(*range(max(-10000000, X-K+1), min(10000001, X+K)))