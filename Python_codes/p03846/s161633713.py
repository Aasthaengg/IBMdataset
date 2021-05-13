from collections import Counter

N = int(input())
A = Counter(list(map(int, input().split())))
mod = 10**9 + 7


if N % 2 == 0:
    for key, value in A.items():
        if key % 2 != 1:
            print(0)
            exit()
    for i in range(1, N, 2):
        if A[i] != 2:
            print(0)
            exit()
    print(pow(2, N//2, mod))
else:
    if A[0] != 1:
        print(0)
        exit()
    for key, value in A.items():
        if key % 2 != 0:
            print(0)
            exit()
    for i in range(2, N, 2):
        if A[i] != 2:
            print(0)
            exit()
    print(pow(2, N // 2, mod))

