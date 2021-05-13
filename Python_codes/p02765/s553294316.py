N, R = map(int, input().split())

if N >= 10:
    print(R)
else:
    total = 100 * (10 - N)
    total = R + total
    print(total)