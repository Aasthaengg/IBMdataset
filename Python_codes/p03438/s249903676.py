N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

n = 0
for j in range(N):
    if B[j] < A[j]:
        n += A[j] - B[j]
        B[j] = A[j]
    elif (B[j] - A[j]) % 2 == 1:
        n += 1
        B[j] += 1

s = sum([b - a for a, b in zip(A, B)])
print("Yes" if s % 2 == 0 and s >= 2 * n else "No")