def actual(N, D, X, A):
    # 2 * [食べたチョコ] + 1 <= D かつ [食べたチョコ]は左の式を超えない整数 を解けばよい
    count_chocolates = lambda a_i: (D - 1) // a_i + 1

    return X + sum([count_chocolates(a_i) for a_i in A])

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

print(actual(N, D, X, A))
