while True:
    n, x = map(int, input().split())
    if (n, x) == (0, 0):
        break
    ways = {tuple(sorted([a, b, c])) for a in range(1, n+1) for b in range(1, n+1) for c in range(1, n+1) if sum((a, b, c)) == x and len({a, b, c}) == 3}
    print(len(ways))