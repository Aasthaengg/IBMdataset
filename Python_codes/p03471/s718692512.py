N, Y = map(int, input().split())
result = [-1, -1, -1]
# a = 0, 1, ..., N
for a in range(0, N + 1):
    # b = 0, 1, ..., N-a
    for b in range(0, N - a + 1):
        c = N - a - b
        if 10000 * a + 5000 * b + 1000 * c == Y:
            result = [a, b, c]
print(*result)