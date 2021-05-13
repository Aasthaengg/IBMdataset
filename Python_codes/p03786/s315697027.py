import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
size = 0
r = 0
ans = 0
for l in range(N):
    if l == r:
        r += 1
        size += A[l]
    while r < N and size * 2 >= A[r]:
        size += A[r]
        r += 1
    if r == N:
        ans += 1
print(ans)