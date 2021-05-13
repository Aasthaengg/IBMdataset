import sys
N, M = map(int, input().split())
ac = [0] * N
wa = [0] * N

for _ in range(M):
    p, s = sys.stdin.readline().split()
    p = int(p) - 1
    if s == "AC":
        ac[p] = 1
    else:
        if not ac[p]:
            wa[p] += 1
acnum = sum(ac)
wanum = sum([c for i, c in enumerate(wa) if ac[i] == 1])
print(acnum, wanum)