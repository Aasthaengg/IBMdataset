N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
INF = 10 ** 9

def dfs(i, a, b, c):
    if i == N:
        if a > 0 and b > 0 and c > 0:
            # 最初の一本目の合体において +10 の必要がないのに足しているので、それぞれについて -10 してあげる
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return INF

    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + l[i], b, c) + 10
    res2 = dfs(i + 1, a, b + l[i], c) + 10
    res3 = dfs(i + 1, a, b, c + l[i]) + 10
    
    return min(res0, res1, res2, res3)

res = dfs(0, 0, 0, 0)
print(res)