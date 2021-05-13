from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
ans_candidate = []
for i in range(1, int(S ** 0.5) + 1):
    if S % i == 0:
        ans_candidate.append(i)
        ans_candidate.append(S // i)


ans = 1
for z in ans_candidate:
    modZ_down = sorted([a % z for a in A])
    modZ_up = sorted([z - mzd for mzd in modZ_down], reverse=True)

    modZ_down = list(accumulate(modZ_down))
    modZ_up = list(accumulate(modZ_up[::-1]))[::-1]

    for i in range(N - 1):
        if (modZ_down[i] == modZ_up[i + 1]) and (modZ_down[i] <= K):
            ans = max(ans, z)

print(ans)
