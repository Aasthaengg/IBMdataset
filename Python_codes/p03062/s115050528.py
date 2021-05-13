N = int(input())
A = list(map(int, input().split()))

min_idx = 0
min_val = float('inf')

for i, a in enumerate(A):
    if abs(a) < min_val:
        min_idx = i
        min_val = abs(a)


for i in range(min_idx):
    if A[i] < 0:
        A[i] *= -1
        A[i + 1] *= -1


for i in range(N - 2, min_idx - 1, -1):
    if A[i + 1] < 0:
        A[i] *= -1
        A[i + 1] *= -1


print(sum(A))
