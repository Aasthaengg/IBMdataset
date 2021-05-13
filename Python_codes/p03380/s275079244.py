def resolve():
    import bisect
    N = int(input())
    A = sorted([int(i) for i in input().split()])
    if N == 2:
        print(max(A), min(A))
        return
    maxA = A[-1]
    half = maxA / 2
    i = bisect.bisect_left(A, half)
    if A[i] - half < half - A[i - 1]:
        print(maxA, A[i])
    else:
        print(maxA, A[i - 1])


resolve()
