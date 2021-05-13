import sys
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n,k = na()
s = 'p'+ns()+'p'
a = 0

for i in range(1,n+1):
    if (s[i] == "L" and s[i-1] == "L") or (s[i] == "R" and s[i+1] == "R"):
        a+=1

print(min(a+2*k,n-1))