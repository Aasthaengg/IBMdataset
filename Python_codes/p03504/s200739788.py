N, C = map(int, input().split())
stc = [None] * N
for i in range(N):
    stc[i] = list(map(int, input().split()))
stc.sort()
recorders = []
for s, t, c in stc:
    ok = False
    for i, rec in enumerate(recorders):
        t2, c2 = rec
        if c == c2 and t2 <= s or c != c2 and t2 < s:
            recorders[i] = [t, c]
            ok = True
            break
    if not ok:
        recorders.append([t, c])
print(len(recorders))
