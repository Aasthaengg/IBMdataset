import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)
N = int(input())
ans = 0
for n in range(N):
    x, u = map(str, input().split())
    x = float(x)
    if not u=='JPY':
        x *= 380000.0
    ans += x
print(ans)