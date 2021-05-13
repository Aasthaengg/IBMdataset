N, M = map(int, input().split())
AC = [False] * (N + 1)
WA = [0] * (N + 1)
for _ in range(M):
    p, S = input().split()
    p = int(p)
    if S =='AC':
        AC[p] = True
    elif S == 'WA' and AC[p] == False:
        WA[p] += 1
print(sum(AC), sum([WA[i] for i, boo in enumerate(AC) if boo]))
