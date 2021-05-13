def resolve():
    N, T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    counts = {}
    a_max = -float("inf")
    a_min = A[0]
    for i in range(1, len(A)):
        if a_min < A[i] and a_max < A[i]:
            a_max = A[i]
            counts.setdefault(a_max-a_min, 0)
            counts[a_max-a_min] += 1
        if a_min > A[i]:
            a_min = A[i]
            a_max = -float("inf")
    #print(counts)
    maxdiff = max(counts.keys())
    print(counts[maxdiff])


if __name__ == '__main__':
    resolve()