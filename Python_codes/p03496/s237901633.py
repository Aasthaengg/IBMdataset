n = int(input())
A = list(map(int, input().split()))

maxim = max(A)
mini = min(A)

if maxim == mini:
    print(0)
    exit()

if abs(maxim) >= abs(mini):
    max_idx = A.index(maxim) + 1
    print(2*n)
    print(max_idx, 1)
    print(max_idx, 1)
    for i in range(1, n):
        print(i, i+1)
        print(i, i+1)

else:
    min_idx = A.index(mini) + 1
    print(2*n)
    print(min_idx, n)
    print(min_idx, n)
    for i in range(n, 1, -1):
        print(i, i-1)
        print(i, i-1)