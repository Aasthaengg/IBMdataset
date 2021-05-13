N, K = map(int, input().split())
A = list(map(int, input().split()))

import math

Asum = sum(A)
candidates = []
for i in range(1, int(math.sqrt(Asum)) + 1):
    if Asum % i == 0:
        candidates.append(i)
        candidates.append(Asum // i)
candidates.sort()

# print("#", Asum)
# print("#", candidates)

ans = 1
for targ in candidates:
    if targ == 1: continue
    A_tmp = [(Ai % targ) for Ai in A]
    # A_tmp.sort(key=lambda x: min((x % targ), ((targ - x) % x)))
    A_tmp.sort()
    idx_l = 0
    idx_r = N - 1
    cnt = 0
    while sum(A_tmp) > 0 and idx_l < idx_r:
        cap_l = A_tmp[idx_l]
        cap_r = targ - A_tmp[idx_r]
        A_tmp[idx_l] = (A_tmp[idx_l] - min(cap_l, cap_r)) % targ
        A_tmp[idx_r] = (A_tmp[idx_r] + min(cap_l, cap_r)) % targ
        cnt += min(cap_l, cap_r)
        if A_tmp[idx_l] == 0:
            idx_l += 1
        if A_tmp[idx_r] == 0:
            idx_r -= 1
    #
    if cnt <= K and sum(A_tmp) == 0: ans = targ

print(ans)