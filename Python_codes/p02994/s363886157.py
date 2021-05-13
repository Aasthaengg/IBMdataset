import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, L = mapint()
apples = [L+i for i in range(N)]
pos_apples = [abs(a) for a in apples]
apples.pop(pos_apples.index(min(pos_apples)))
print(sum(apples))