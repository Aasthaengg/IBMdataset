N = int(input())
A = list(map(int, input().split()))
c = 1
i = 0
while i < N - 1:
    if A[i] < A[i + 1]:
        while True:
            i += 1
            if i == N - 1:
                break
            if A[i] > A[i + 1]:
                c += 1
                i += 1
                break
    elif A[i] > A[i + 1]:
        while True:
            i += 1
            if i == N - 1:
                break
            if A[i] < A[i + 1]:
                c += 1
                i += 1
                break
    elif A[i] == A[i + 1]:
        i += 1
print(c)