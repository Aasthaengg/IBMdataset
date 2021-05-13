D, N = map(int, input().split())

d = 100 ** D * N

if N == 100:
    d += 100 ** D

print(d)
