N = int(input())

v = float("inf")
for a in range(1, N):
    b = N - a
    c = sum(map(int, str(a))) + sum(map(int, str(b)))
    if c < v:
        v = c
print(v)