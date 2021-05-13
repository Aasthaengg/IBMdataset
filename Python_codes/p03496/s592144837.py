def main():
    """
    2<= N <= 50

    a_x += a_y: 2N回まで

    a_1 <= a_2 <= ... <= a_N にする
    """
    N = int(input())
    A = map(int, input().split())
    A = list(A)

    solve(N, A)


def solve(N, A):
    if A == sorted(A):
        print(0)
        return

    p = [i for i, a in enumerate(A) if a >= 0]
    m = [i for i, a in enumerate(A) if a < 0]

    # 調整
    operations = []
    plus = len(p) > 0
    if p and m:
        p_max_a = max(A[i] for i in p)
        m_min_a = min(A[i] for i in m)

        if abs(m_min_a) > abs(p_max_a):
            idx_list = p
            idx = A.index(m_min_a)
        else:
            idx_list = m
            idx = A.index(p_max_a)

        for i in idx_list:
            A[i] += A[idx]
            operations.append((idx+1, i+1))

    if sum(A) >= 0:
        for i in range(1, N):
            operations.append((i, i+1))
            A[i] += A[i-1]
    else:
        for i in range(N-1, 0, -1):
            operations.append((i+1, i))
            A[i-1] += A[i]

    print(len(operations))
    for src, dst in operations:
        print(src, dst)

    debug = False
    if debug:
        print(A)
        assert A == sorted(A)
        assert len(operations) <= N * 2


if __name__ == '__main__':
    main()
