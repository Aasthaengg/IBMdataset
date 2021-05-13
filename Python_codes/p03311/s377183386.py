import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

As = [a-i for i, a in enumerate(As, 1)]
As.sort()
middle = As[N//2]
print(sum([abs(a-middle) for a in As]))