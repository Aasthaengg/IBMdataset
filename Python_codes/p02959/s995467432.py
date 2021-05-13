import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

ans = 0
plus = 0
for i in range(N):
    if A[i] >= plus:
        A[i] -= plus
        ans += plus
    else:
        ans += A[i]
        A[i] = 0
    plus = 0

    if A[i] >= B[i]:
        ans += B[i]
    else:
        ans += A[i]
        plus = B[i] - A[i]
    # print(ans, plus)

if A[N] >= plus:
    ans += plus
else:
    ans += A[N]

print(ans)