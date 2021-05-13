import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S, T = input().split()
ans = ''
for s, t in zip(list(S), list(T)):
    ans += s+t
print(ans)