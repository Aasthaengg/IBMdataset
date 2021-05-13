n = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(1, n - 1):
    if A[i - 1] > A[i] > A[i + 1] or A[i - 1] < A[i] < A[i + 1]:
        ans = ans + 1

print(ans)