A = sorted(list(map(int, input().split())), reverse=True)

if all([i % 2 == 0 for i in A]) or all([i % 2 == 1 for i in A]):
    print((A[0] - A[1] + A[0] - A[2]) // 2)
else:
    if [i % 2 == 0 for i in A].count(True) == 2:
        for i in range(3):
            if A[i] % 2 == 0:
                A[i] += 1
        print((A[0] - A[1] + A[0] - A[2]) // 2 + 1)
    else:
        for i in range(3):
            if A[i] % 2 == 1:
                A[i] += 1
        print((A[0] - A[1] + A[0] - A[2]) // 2 + 1)