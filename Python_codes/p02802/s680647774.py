N, M = map(int, input().split())
accept = set()
penalty = 0
wa_cnt = [0] * N

for m in range(M):
    p, s = input().split()
    p = int(p) -1 
    if p in accept:
        continue
    elif s == 'AC':
        accept.add(p)
        penalty += wa_cnt[p]
    else:
        wa_cnt[p] += 1

print(len(accept), penalty)

