def main():
    from itertools import cycle
    from operator import add, sub

    N = int(input())
    *A, = map(int, input().split())

    cycl_oper = cycle((add, sub))

    M0 = 0  # 山0(0-ind)への降雨量
    for op, x in zip(cycl_oper, A):
        M0 = op(M0, x)

    ans = [0] * N
    ans[0] = M0
    for i in range(1, N):
        ans[i] = A[i - 1] * 2 - ans[i - 1]

    print(*ans)


if __name__ == '__main__':
    main()
