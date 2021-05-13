N = int(input())

A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

A.sort()
B.sort()

if N % 2 == 0:
    n1 = N // 2 - 1
    n2 = N // 2
    ans = B[n1] - A[n1] + B[n2] - A[n2] + 1
    print(ans)

else:
    n = N // 2
    ans = B[n] - A[n] + 1
    print(ans)