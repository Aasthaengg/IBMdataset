N, M, C = map(int, input().strip().split(" "))
B = list(map(int, input().strip().split(" ")))
count = 0

for _ in range(N):
    A = list(map(int, input().strip().split(" ")))
    s = 0
    for a, b in zip(A, B):
        s += a * b
    s += C
    if s > 0:
        count += 1

print(count)