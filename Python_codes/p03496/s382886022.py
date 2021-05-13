def judge(L):
    cnt_plus = 0
    cnt_minus = 0
    for l in L:
        if l >= 0:
            cnt_plus += 1
        else:
            cnt_minus += 1

    if cnt_plus == len(L):
        return 1
    elif cnt_minus == len(L):
        return -1
    else:
        return 0


def solve():
    N = int(input())
    A = list(map(int, input().split(" ")))

    if judge(A) == 1:
        print(N - 1)
        for i in range(1, N):
            print(i, i + 1)
    elif judge(A) == -1:
        print(N - 1)
        for i in range(N, 1, -1):
            print(i, i - 1)
    elif judge(A) == 0:
        print(2 * N - 1)
        MAX = max(A)
        MAX_INDEX = A.index(MAX) + 1
        MIN = min(A)
        MIN_INDEX = A.index(MIN) + 1
        if abs(MAX) >= abs(MIN):
            for i in range(1, N + 1):
                print(MAX_INDEX, i)
            for i in range(1, N):
                print(i, i + 1)
        elif abs(MAX) < abs(MIN):
            for i in range(1, N + 1):
                print(MIN_INDEX, i)
            for i in range(N, 1, -1):
                print(i, i - 1)


solve()