import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = str(input())
T = str(input())
ans = 0
for i in range(3):
    if S[i]==T[i]:
        ans += 1
print(ans)