import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
ans = 0
for i in range(1, N+1):
    if len(str(i))%2==1:
        ans += 1
print(ans)