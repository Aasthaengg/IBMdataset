import sys

N, x = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
tmp_sum = A[0]
for i in range(N-1):
    if A[i] + A[i+1] > x:
        diff = A[i] + A[i+1] - x
        ans += diff
        # 明示的に書かれていないが、A[i] > diff - A[i+i]  はないはず
        A[i+1] = 0 if A[i+1] < diff else A[i+1] - diff

print(ans)