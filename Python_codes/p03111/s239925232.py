def li():
    return [int(x) for x in input().split()]
INF = 10**18
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, A, B, C = li()
l = [int(input()) for x in range(N)]

def dfs(index, a, b, c, none):
    # 終端
    if index == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C)
        else:
            return INF
    # ツリー構造
    v1 = dfs(index+1, a + l[index], b, c, none) + (10 if a > 0 else 0)
    v2 = dfs(index+1, a, b + l[index], c, none) + (10 if b > 0 else 0)
    v3 = dfs(index+1, a, b, c + l[index], none) + (10 if c > 0 else 0)
    v4 = dfs(index+1, a, b, c, none+1)
    return min(v1, v2, v3, v4)

ans = dfs(0, 0, 0, 0, 0)
print(ans)