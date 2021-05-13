def check(arr, mid, maxV):
    if arr[mid] < maxV:
        return True
    else:
        return False


def binSearch(arr, maxV):
    ok = -1
    ng = len(arr)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(arr, mid, maxV):
            ok = mid
        else:
            ng = mid
    return ok


def resolve():
    N = int(input())
    A = sorted([int(i) for i in input().split()])
    B = sorted([int(i) for i in input().split()])
    C = sorted([int(i) for i in input().split()])
    BoverA = [0 for _ in range(N)]
    sumA = 0
    for i in range(N):
        a = binSearch(A, B[i])
        sumA += (a + 1)
        BoverA[i] = sumA
    sumA = 0
    for i in range(N):
        b = binSearch(B, C[i])
        if b >= 0:
            sumA += 1 * 1 * BoverA[b]
    print(sumA)


resolve()
