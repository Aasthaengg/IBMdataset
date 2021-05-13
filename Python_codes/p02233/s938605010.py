def resolve():
    n = int(input())
    A = [1, 1]
    for i in range(1, 45):
        A.append(A[i - 1] + A[i])
    print(A[n])


resolve()

