N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

count = 0
for A in A:
    ans = C
    for a, b in zip(A, B):
        ans += a * b
    if ans > 0:
        count += 1
print(count)