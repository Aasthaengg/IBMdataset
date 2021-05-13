n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
INF = 10**9

def rec(cur, a, b, c):
    if cur == n:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else INF
    ret0 = rec(cur+1, a, b, c)
    ret1 = rec(cur+1, a+L[cur], b, c) + 10
    ret2 = rec(cur+1, a, b+L[cur], c) + 10
    ret3 = rec(cur+1, a, b, c+L[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

print(rec(0, 0, 0, 0))
