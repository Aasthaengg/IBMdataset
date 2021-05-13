N, M = [int(s) for s in input().split()]
AC = [0] * 10 ** 5
WA = [0] * 10 ** 5

wa = 0
for _ in range(M):
    p, s = input().split()
    p = int(p)
    if AC[p] == 0:
        if s == 'WA':
            WA[p] += 1
        else:
            AC[p] += 1

print(sum(AC), sum(map(lambda x: x[0] * x[1], zip(AC, WA))))