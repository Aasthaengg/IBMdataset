n, m = list(map(int, input().split()))
connects = [0] * n
for _ in range(m):
    a, b = list(map(int, input().split()))
    connects[a - 1] += 1
    connects[b - 1] += 1
[print(c) for c in connects]