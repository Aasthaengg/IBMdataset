import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
K = int(input())
now = 1
for _ in range(N):
    now = min(now*2, now+K)
print(now)