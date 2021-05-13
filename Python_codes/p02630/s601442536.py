N = int(input())
A = list(map(int, input().split()))
total = sum(A)
d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]
for b, c in BC:
    if b in d:
        total += d[b] * (c-b)
        if c in d:
            d[c] += d[b]
        else:
            d[c] = d[b]
        d[b] = 0
    print(total)