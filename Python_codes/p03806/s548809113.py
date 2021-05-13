import fractions


def args():
    N, MA, MB = list(map(int, input().split()))

    A, B, C = [], [], []
    for i in range(N):
        a, b, c = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        C.append(c)

    # print(N, MA, MB)
    # print(A)
    # print(B)
    # print(C)

    return N, MA, MB, A, B, C

def solve(N, MA, MB, A, B, C):
    def recur(i, a, b):
        if not MEMO[i][a][b] is None:
            return MEMO[i][a][b]

        if not i < N:
            if 0 < a and 0 < b:
                g = fractions.gcd(a, b)
                if (MA, MB) == (a / g, b / g):
                    return 0
            return float("inf")

        res = min(recur(i + 1, a, b) + 0, recur(i + 1, a + A[i], b + B[i]) + C[i])
        MEMO[i][a][b] = res
        return res

    x, y, z = N + 1, 10 * N + 1, 10 * N + 1
    MEMO = [[[None] * z for _ in range(y)] for _ in range(x)]

    ans = recur(0, 0, 0)

    return ans


if __name__ == '__main__':
    res = solve(*args())

    print(-1) if res == float("inf") else print(res)
