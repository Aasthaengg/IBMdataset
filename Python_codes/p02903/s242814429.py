def solve(h, w, a, b):
    A = [[0]*w for _ in range(h)]
    for r in range(b):
        for c in range(a):
            A[r][c] = 1
    for r in range(b, h):
        for c in range(a, w):
            A[r][c] = 1
    return "\n".join(["".join(map(str, A[r])) for r in range(h)])

h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))