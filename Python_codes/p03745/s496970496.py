N = int(input())
A = list(map(int, input().split()))


p = 0
res = 0

while p < N:
    while p + 1 < N and A[p] == A[p + 1]:
        p += 1
    if p + 1 < N and A[p] < A[p + 1]:
        while p + 1 < N and A[p] <= A[p + 1]:
            p += 1
    elif p + 1 < N and A[p] > A[p + 1]:
        while p + 1 < N and A[p] >= A[p + 1]:
            p += 1
    res += 1
    p += 1
print(res)
