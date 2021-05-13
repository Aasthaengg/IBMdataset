N = int(input())
A = [int(x) for x in input().split()]

min_A = min(A)
max_A = max(A)

if min_A == max_A:
    print(0)
elif max_A < 0:
    print(N - 1)
    for i in range(N - 1, 0, -1):
        print(i + 1, i)
elif min_A > 0:
    print(N - 1)
    for i in range(N - 1):
        print(i + 1, i + 2)
else:
    if abs(min_A) > max_A:
        index = A.index(min_A)
    else:
        index = A.index(max_A)

    print(2 * N - 1)
    for i in range(N):
        print(index + 1, i + 1)

    if abs(min_A) > max_A:
        for i in range(N - 1, 0, -1):
            print(i + 1, i)
    else:
        for i in range(N - 1):
            print(i + 1, i + 2)
