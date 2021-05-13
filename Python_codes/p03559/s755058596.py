import sys
from bisect import bisect_left

input = sys.stdin.buffer.readline
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

cumsum = [0]
for i in range(len(B)):
    b = B[i]
    a_idx = bisect_left(A, b)
    cumsum.append(cumsum[i] + a_idx)
# print('cumsum', cumsum)

ans = 0
for i in range(len(C)):
    c = C[i]
    b_idx = bisect_left(B, c)
    ans += cumsum[b_idx]
print(ans)
