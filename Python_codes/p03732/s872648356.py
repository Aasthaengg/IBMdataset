from itertools import accumulate
N, W = map(int, input().split())
V = [[] for _ in range(4)]
w0, v0 = map(int, input().split())
V[0].append(v0)
for _ in range(N - 1):
    w, v = map(int, input().split())
    V[w - w0].append(v)
S = []
for v in V:
    v.sort(reverse=True)
    S.append([0] + list(accumulate(v)))
ans = 0
for i, si in enumerate(S[0]):
    for j, sj in enumerate(S[1]):
        for k, sk in enumerate(S[2]):
            for l, sl in enumerate(S[3]):
                if w0 * i + (w0 + 1) * j + (w0 + 2) * k + (w0 + 3) * l > W:
                    continue
                ans = max(ans, si + sj + sk + sl)
print(ans)
