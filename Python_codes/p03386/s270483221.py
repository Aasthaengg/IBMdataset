a, b, k = map(int, input().split())
if b - a + 1 <= k * 2:
    print(*range(a, b + 1), sep="\n")
else:
    print(*range(a, a + k), sep="\n")
    print(*range(b - k + 1, b + 1), sep="\n")