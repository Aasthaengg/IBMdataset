# coding: utf-8
# 全探索


def solve(i, m):
    global A, n

    if (m == 0):
        return True
    if (i >= n):
        return False

    res = solve(i + 1, m) or solve(i + 1, m - A[i])

    return res


if __name__ == "__main__":
    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    m = [int(i) for i in input().split()]
    total = sum(A)
    for m_i in m:
        if m_i > total:
            print('no')
        else:
            print('yes' if solve(0, m_i) else 'no')

