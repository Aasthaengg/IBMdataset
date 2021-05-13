N, M = list(map(int, input().split()))
p = [0]*M
S = [0]*M

for i in range(M):
    inp = input().split()
    p[i], S[i] = int(inp[0]), inp[1]

is_ac = [False]*N
wa_cnt = [0]*N

for i in range(M):
    if S[i] == 'AC':
        is_ac[p[i]-1] = True
    else:
        if not is_ac[p[i]-1]:
            wa_cnt[p[i]-1] += 1

ac_cnt = 0
penalty = 0

for j in range(N):
    if is_ac[j]:
        ac_cnt += 1
        penalty += wa_cnt[j]

print("{} {}".format(ac_cnt, penalty))