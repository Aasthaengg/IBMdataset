import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

A.sort()

acum = 0
ans = 0
for i in range(N-1):
    acum += A[i]
    if acum * 2 >= A[i+1]:
        ans += 1
    else:
        ans = 0

print(ans+1)