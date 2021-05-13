N, K = map(int, input().split())
S = input()
segs = []
prev = "x"
for c in S:
    if c != prev:
        segs.append([c])
    else:
        segs[-1].append(c)
    prev = c
ans = sum(len(seg) - 1 for seg in segs)
print(min(ans + 2 * K, N - 1))
