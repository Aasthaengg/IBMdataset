x, n = map(int, input().split())
P = list(map(int, input().split()))

for d in range(x + 1):
    for s in [-1, +1]:
        a = x + s * d
        if P.count(a) == 0:
            print(a)
            exit(0) 