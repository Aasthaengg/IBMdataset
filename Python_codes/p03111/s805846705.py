# coding: utf-8
import sys
sys.setrecursionlimit(10**9)
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
N, A, B, C = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))
# L.sort()
def dfs(cnt, a, b, c):
    if cnt == N:
        return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a,b,c) > 0 else 10**9
    r0 = dfs(cnt+1, a, b, c)
    r1 = dfs(cnt+1, a+L[cnt], b, c) + 10
    r2 = dfs(cnt+1, a, b+L[cnt], c) + 10
    r3 = dfs(cnt+1, a, b, c+L[cnt]) + 10
    return min(r0, r1, r2, r3)
    
print(dfs(0,0,0,0))