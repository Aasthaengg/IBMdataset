n = int(input())
A = list(map(int, input().split()))
goukei = sum(A)
jama = 0

for i in range(n // 2):
    jama += A[2 * i + 1]

ans = [0] * n

ans[0] = goukei - jama * 2

for i in range(1, n):
    ans[i] = 2 * A[i - 1] - ans[i - 1]

print(*ans, sep=" ")
