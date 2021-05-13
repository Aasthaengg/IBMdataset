N = int(input())
A = list(map(int, input().split()))
A.sort()
B = [0] * N
B[0] = A[0]
for i in range(1, N):
    B[i] = B[i - 1] + A[i]

ans = 1
for i in range(N - 2, -1, -1):
    if A[i + 1] <= 2 * B[i]:
        ans += 1
    else:
        break

print(ans)
