from itertools import product
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 10 ** 18
for alloc in product(range(4), repeat=N):
    La = 0
    Lb = 0
    Lc = 0
    use_a = 0
    use_b = 0
    use_c = 0
    for i, f in enumerate(alloc):
        if f == 0:
            La += L[i]
            use_a += 1
        elif f == 1:
            Lb += L[i]
            use_b += 1
        elif f == 2:
            Lc += L[i]
            use_c += 1
        else:
            pass

    if not all([use_a, use_b, use_c]):
        continue

    score = 0
    score += 10 * (use_a - 1)
    score += 10 * (use_b - 1)
    score += 10 * (use_c - 1)
    score += abs(A - La)
    score += abs(B - Lb)
    score += abs(C - Lc)
    ans = min(ans, score)

print(ans)