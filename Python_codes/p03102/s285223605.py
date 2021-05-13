N, M, C = map(int, input().split())
B = list(map(int, input().split()))

ok_count = 0
for _ in range(N):
    A = list(map(int, input().split()))
    total = 0
    for a, b in zip(A, B):
        total += a * b
    total += C
    if total > 0:
        ok_count += 1
print(ok_count)