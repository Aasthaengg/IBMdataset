def resolve():
    N, x = list(map(int, input().split()))
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-1):
        if A[i] + A[i+1] > x:
            diff = (A[i] + A[i+1]) - x
            cnt += diff
            if A[i+1] < diff:
                A[i] = diff - A[i+1]
                A[i+1] = 0
            else:
                A[i+1] -= diff
    print(cnt)


if '__main__' == __name__:
    resolve()

