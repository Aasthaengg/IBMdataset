
def solve():
    N = int(raw_input())
    A = [int(_) for _ in raw_input().split()]
    A.sort()
    ret = abs(A[N-1] - A[0])
    rever = [0] * (N - 1)
    for i in range(1, N-1):
        if A[i] >= 0:
            ret = ret + A[i]
            rever[i-1] = 1
        else:
            ret = ret - A[i]
    print ret
    def PrintAndCalcSave(a, b, rever):
        if rever == 0:
            print a, b
            return a - b
        else:
            print b, a
            return b - a

    cnt = 0
    if A[N-1] > A[0]:
        save = PrintAndCalcSave(A[N-1], A[0], rever[cnt])
    else:
        save = PrintAndCalcSave(A[0], A[N-1], rever[cnt])
    cnt += 1
    for i in range(1, N - 1):
        if A[i] >= 0:
            save = PrintAndCalcSave(A[i], save, rever[cnt])
        else:
            save = PrintAndCalcSave(save, A[i], rever[cnt])
        cnt += 1

if __name__ == '__main__':
    solve()
