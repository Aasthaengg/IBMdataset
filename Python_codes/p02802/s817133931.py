n, m = map(int, input().split())
S = [[] for _ in range(n)]
pe = [0] * n
co = [0] * n
for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    S[p] += [s]
for i, s_ in enumerate(S):
    if all(j == 'WA' for j in s_):
        continue
    for s in s_:
        if s == 'AC':
            co[i] = 1
            break
        else:
            pe[i] += 1
print(sum(co), sum(pe))
