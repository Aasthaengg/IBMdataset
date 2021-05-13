import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

s = ns()
a = ord('a')

al = [chr(i) for i in range(ord('a'), ord('z')+1)]
ans = 100

for c in al:
    L = list(s.split(c))
    x = 0
    for y in L:
        x = max(x,len(y))
    ans = min(x,ans)

print(ans)