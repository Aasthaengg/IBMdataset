from itertools import product
def main():
    N, M = map(int, input().split())
    CAKES = [tuple(map(int, input().split())) for _ in range(N)]
    m = 0
    for a, b, c in product([1, -1], repeat=3):
        C = [x * a + y * b + z * c for x, y, z in CAKES]
        C.sort(reverse=True)
        m = max(m, sum(C[:M]))
    return m

print(main())
