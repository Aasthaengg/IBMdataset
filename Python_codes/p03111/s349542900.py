N, A, B, C = list(map(int,input().split()))
l = [int(input()) for _ in range(N)]

def dfs(i, a, b, c):
    if i == N:
        if a and b and c:
            return abs(a - A) + abs(b - B) + abs(c - C)
        else:
            return 10 ** 9 + 7
    else:
        ret1 = dfs(i + 1, a + l[i], b, c) + 10
        ret2 = dfs(i + 1, a, b + l[i], c) + 10
        ret3 = dfs(i + 1, a, b, c + l[i]) + 10
        ret4 = dfs(i + 1, a, b, c)
        ret = min(ret1, ret2, ret3, ret4)
        return ret
    
ans = dfs(0, 0, 0, 0)
print(ans - 30)