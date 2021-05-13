def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    c = -1
    r = 0
    for a, b in AB:
        if a >= c:
            c = b
            r += 1
    return r

print(main())
