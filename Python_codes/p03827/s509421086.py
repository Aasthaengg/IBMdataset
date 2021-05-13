import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())
ans = 0
x = 0
for s in S:
    if s=='I':
        x+=1
        ans = max(x, ans)
    else:
        x-=1
        ans = max(x, ans)
print(ans)