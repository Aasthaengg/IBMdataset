N, R = [int(s) for s in input().split()]

r = R
if N < 10:
    r += 100 * (10 - N)
print(r)