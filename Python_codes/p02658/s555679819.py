N = int(input().rstrip())
A = sorted([int(v) for v in input().rstrip().split()])

r = 1
for v in A:
    if v == 0:
        r = 0
        break

    r *= v
    if r > 1000000000000000000:
        r = -1
        break

print(r)

