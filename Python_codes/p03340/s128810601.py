import sys

read = sys.stdin.buffer.read


N, *A = map(int, read().split())

ans = 0
right = 0
s = 0

for left in range(N):
    while right < N and s & A[right] == 0:
        s ^= A[right]
        right += 1

    ans += right - left

    if left == right:
        right += 1
    else:
        s ^= A[left]

print(ans)

