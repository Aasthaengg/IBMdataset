import sys
input = sys.stdin.buffer.readline
N = int(input())
A = list(map(int, input().split()))
d = 0
ans = 1
for i in range(1, N):
    if A[i - 1] < A[i]:
        if d < 0:
            ans += 1
            d = 0
        elif d == 0:
            d = 1
    elif A[i - 1] > A[i]:
        if d > 0:
            ans += 1
            d = 0
        elif d == 0:
            d = -1
print(ans)
