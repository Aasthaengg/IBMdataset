N, K = map(int, input().split())
S = input()
assert len(S) == N
first = S[0]
target = "R" if first == "L" else "L"


def count_unhappy():
    tcnt = 0
    consecutive = False
    for c in S:
        if c == target:
            consecutive = True
        elif consecutive:
            tcnt += 1
            consecutive = False
    if consecutive:
        tcnt += 1
    unhappy = 2 * tcnt + (0 if S[-1] == target else 1)
    return max(unhappy - 2 * K, 1)


print(N - count_unhappy())
