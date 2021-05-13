r, c = map(int, input().split())
R = [0] * (c + 1)
i = 0
while i < r:
    n = list(map(int, input().split()))
    n.append(sum(n))
    R = [x + y for (x, y) in zip(R, n)]
    print(' '.join(map(str, n)))
    i += 1
print(' '.join(map(str, R)))