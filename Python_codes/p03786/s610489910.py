import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()
# print(A)
ans = 0

acum = 0
for i in range(N-1):
    acum += A[i]
    if acum * 2 < A[i+1]:
        ans = 0
    else:
        ans += 1

print(ans + 1)