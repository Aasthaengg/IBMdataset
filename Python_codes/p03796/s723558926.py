import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
mod = 10**9+7
ans = 1
for i in range(1, N+1):
    ans *= i
    ans %= mod
print(ans)