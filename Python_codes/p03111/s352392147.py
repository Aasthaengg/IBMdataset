N, A, B, C = [int(i) for i in input().split()]
l = [int(input()) for _ in range(N)]
INF = 10**9


def dfs(depth, a, b, c):
    if depth == N:
        # A, B, C いずれも竹は1本以上必ず使っていないとだめ
        if min(a, b, c) > 0:
            # 合体が終わったあとで差を計算してそれがコストになる
            return abs(a-A) + abs(b-B) + abs(c-C) - 30
        else:
            return INF

    # 今ある竹を採用しない場合
    ret0 = dfs(depth + 1, a, b, c)

    # A, B, C を使う場合
    # 先にまとめて合体してあとで -30 することによって調整
    ret1 = dfs(depth + 1, a + l[depth], b, c) + 10
    ret2 = dfs(depth + 1, a, b + l[depth], c) + 10
    ret3 = dfs(depth + 1, a, b, c + l[depth]) + 10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
