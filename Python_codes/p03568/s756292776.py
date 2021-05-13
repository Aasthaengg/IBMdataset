import sys
sys.setrecursionlimit(500*500)
n = int(input())
a = list(map(int, input().split()))
ans = 0

def dfs(i, p, sum):
    global ans
    if p == n:
        if sum % 2 == 0:
            ans += 1
    else:
        dfs(a[p], p+1, sum*a[p])
        dfs(a[p]+1, p+1, sum*(a[p]+1))
        dfs(a[p]-1, p+1, sum*(a[p]-1))

dfs(1, 0, 1)
print(ans)
