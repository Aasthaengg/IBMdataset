N = int(input())
P = [int(input()) for _ in range(N)]
vi = {v: i for i, v in enumerate(P)}
incmax = inc = 1
before = vi[1]
for v in range(2, N + 1):
    if vi[v] > before:
        inc += 1
    else:
        inc = 1
    incmax = max(incmax, inc)
    before = vi[v]
print(N - incmax)