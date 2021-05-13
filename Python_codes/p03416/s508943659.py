import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()

ans = 0
for i in range(A, B+1):
    s = str(i)
    if s[0]==s[-1] and s[1]==s[-2]:
        ans += 1
print(ans)