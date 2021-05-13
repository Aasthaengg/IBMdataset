N, M = map(int, input().split())
ac = [0 for i in range(N)]
wa = [0 for i in range(N)]
for _ in range(M):
    p, s = input().split()
    if s == "AC":
        ac[int(p)-1] = 1
    elif s == "WA":
        if ac[int(p)-1] != 1:
            wa[int(p)-1] += 1
print(sum(ac), sum([i*j for i, j in zip(ac, wa)]))
