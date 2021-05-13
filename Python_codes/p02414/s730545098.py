def print_matrix(m):
    for cnt in range(len(m)):
        print(" ".join(map(str, m[cnt])))


def mul(lhs, rhs):
    n = len(lhs)
    m = len(rhs)
    l = len(rhs[0])

    ret = [
        [
            sum([lhs[i][k] * rhs[k][j] for k in range(m)])
            for j in range(l)
            ]
        for i in range(n)
        ]

    return ret


if __name__ == '__main__':
    from sys import stdin

    n, m, l = (int(_) for _ in stdin.readline().rstrip().split())

    A = []
    for _ in range(n):
        A.append([int(_) for _ in stdin.readline().rstrip().split()])

    B = []
    for _ in range(m):
        B.append([int(_) for _ in stdin.readline().rstrip().split()])

    C = mul(A, B)

    print_matrix(C)

