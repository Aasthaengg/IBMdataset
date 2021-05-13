import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
ans = 0
for i in range(1, N+1):
    cnt = 0
    while i*(2**cnt)<K:
        cnt += 1
    ans += 1/(2**cnt)
print(ans/N)