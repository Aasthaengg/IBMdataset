N, C = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

P.sort()

rec = []
rec_cha = [None] * C
for s, t, c in P:
    c -= 1
    if rec_cha[c] is None:
        for i, (pt, pc) in enumerate(rec):
            if pt < s:
                rec[i] = (t, c)
                rec_cha[pc] = None
                rec_cha[c] = i
                break
        else:
            rec.append((t, c))
            rec_cha[c] = len(rec) - 1
    else:
        rec[rec_cha[c]] = (t, c)

print(len(rec))
