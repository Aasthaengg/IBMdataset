N, K = map(int, input().split())
S = input()

cnt = 0
for s, s_ in zip(S, S[1:]):
    if s == s_:
        cnt += 1

unhappy = N - 1 - cnt

print(cnt + min(unhappy, 2 * K))
