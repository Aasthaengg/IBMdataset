K = int(input())
A = list(map(int, input().split()))
min = 2
max = 2
for i in range(K-1, -1, -1):
    if max < A[i]:
        print(-1)
        exit()
    min = (min + A[i] - 1) // A[i] * A[i]
    max = (max // A[i] + 1) * A[i] - 1
    if max < min:
        print(-1)
        exit()
print(min, max)
