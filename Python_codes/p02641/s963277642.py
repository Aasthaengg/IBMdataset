X, N = map(int, input().split())
if N > 0:
    P = set(map(int, input().split()))
else:
    P = set()

d = 0
while True:
    for sign in [-1, 1]:
        cand = X + sign * d
        if cand not in P:
            print(cand)
            exit()
    d += 1

