N = int(input())
A = [int(num) for num in input().split()]

ans = 0

for i in range(N-1):
    if A[i] - A[i+1] > 0:
        ans += A[i] - A[i+1]
        A[i+1] = A[i]


print(ans)