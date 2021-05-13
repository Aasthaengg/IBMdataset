


def solve(N, AB):
    def getMedian(A):
        if N % 2 == 0:
            m1 = A[N // 2 - 1]
            m2 = A[N // 2]
            m = (m1 + m2) / 2
        else:
            m = A[N // 2]
        return m

    A = sorted(a for a, b in AB)
    B = sorted(b for a, b in AB)
    if N % 2 == 0:
        return int(2 * (getMedian(B) - getMedian(A))) + 1
    else:
        return getMedian(B) - getMedian(A) + 1


(N,) = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for i in range(N)]
print(solve(N, AB))
