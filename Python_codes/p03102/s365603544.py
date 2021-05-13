N, M, C = map(int, input().split())
B = list(map(int, input().split()))
n = 0
for _ in range(N):
    Ai = list(map(int, input().split()))
    s = C
    for a, b in zip(Ai, B):
        s += a * b
    if s > 0:
        n += 1
print(n)
