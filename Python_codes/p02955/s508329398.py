from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = sum(A)


ans_candidates = []
for n in range(1, int(M ** 0.5) + 1):
    if M % n == 0:
        ans_candidates.append(n)
        ans_candidates.append(M // n)


ans = 0
for X in ans_candidates:
    need_plus = sorted([(X - a % X) % X for a in A])
    need_minus = [X - nm for nm in need_plus]

    need_plus = list(accumulate(need_plus))
    need_minus = list(accumulate(need_minus))

    for i in range(N):
        if need_plus[i] > K:
            break

        if need_plus[i] == (need_minus[-1] - need_minus[i]):
            ans = max(ans, X)
            break

print(ans)
