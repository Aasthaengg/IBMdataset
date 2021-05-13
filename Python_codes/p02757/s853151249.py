from collections import Counter


N, P = map(int, input().split())
S = input()

cnt = 0
if P in [2, 5]:
    for i, s in enumerate(S):
        if int(s) % P == 0:
            cnt += (i + 1)
else:
    T = [0] * (N + 1)
    mods = Counter({0: 1})
    for i, s in enumerate(reversed(S)):
        T[N - 1 - i] = (T[N - i] + int(s) * pow(10, i, P)) % P
        mods[T[N - 1 - i]] += 1
    for t in T:
        mods[t] -= 1
        cnt += mods[t]

print(cnt)
