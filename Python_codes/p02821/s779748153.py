from itertools import accumulate
from operator import mul
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (10 ** 5 * 2 + 1)
for a in A:
    B[a] += 1
C = list(accumulate(B[::-1]))[::-1]
l, r = 1, 10 ** 5 * 2 + 1
while r - l > 1:
    m = l + (r - l + 1) // 2
    if sum(C[max(0, m - a)] for a in A) >= M:
        l = m
    else:
        r = m
D = list(accumulate(map(mul, range(10 ** 5 * 2, -1, -1), B[::-1])))[::-1]
ans = sum(D[max(0, l - a)] - (l - a) * C[max(0, l - a)] for a in A) + l * M
print(ans)