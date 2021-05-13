N, K = map(int, input().split())
S = input()
assert len(S) == N


def count_unhappy():
    tcnt = 0
    consecutive = False
    for c in S:
        if c != S[0]:
            consecutive = True
        elif consecutive:
            tcnt += 1
            consecutive = False
    if consecutive:
        tcnt += 1
    unhappy = 2 * tcnt + (0 if S[-1] != S[0] else 1)
    return max(unhappy - 2 * K, 1)


print(N - count_unhappy())
