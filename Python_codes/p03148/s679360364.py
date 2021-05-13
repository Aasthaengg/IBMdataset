from collections import defaultdict

N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

TD.sort(key = lambda x: -x[1])
#print(TD)

tmp = [[] for _ in range(N + 1)]
cnt = defaultdict(int)
out_candidate = []
kiso = 0
kind = 0
for i in range(K):
    t, d = TD[i]
    tmp[t].append(d)
    if cnt[t]:
        out_candidate.append([t, d])
    else:
        kind += 1
    kiso += d
    cnt[t] += 1
out_candidate.sort(key = lambda x: -x[1])
#print(tmp)
#print(cnt)
#print(out_candidate)
#print(kiso, kind)

answer = []
answer.append(kiso + kind ** 2)

in_candidate = []
if K < N:
    for i in range(K, N):
        in_candidate.append(TD[i])
in_candidate.sort(key = lambda x: x[1])
#print(in_candidate)

while out_candidate and in_candidate:
    in_t, in_d = in_candidate.pop()
    if cnt[in_t] == 0:
        cnt[in_t] += 1
        out_t, out_d = out_candidate.pop()
        kiso += in_d - out_d
        kind += 1
        answer.append(kiso + kind ** 2)
        
print(max(answer))