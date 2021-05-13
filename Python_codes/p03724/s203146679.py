from itertools import accumulate

N, M = map(int, input().split())
acc = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    acc[a - 1] += 1
    acc[b - 1] -= 1
print("NO") if any(a % 2 for a in accumulate(acc)) else print("YES")
