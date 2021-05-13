N = int(input())
A = list(map(int, input().split()))

s = sum([A[i] * (-1) ** i for i in range(N)])

for i in range(1, N + 1):
    print(s)
    s = 2 * A[i - 1] - s