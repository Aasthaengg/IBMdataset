from itertools import product, accumulate

N, W = map(int, input().split())
v0, v1, v2, v3 = [None], [], [], []
w0, v0[0] = map(int, input().split())
for i in range(1, N):
    w, v = map(int, input().split())
    if w - w0 == 0:
        v0.append(v)
    elif w - w0 == 1:
        v1.append(v)
    elif w - w0 == 2:
        v2.append(v)
    else:
        v3.append(v)

v0 = sorted(v0, reverse=True)
v1 = sorted(v1, reverse=True)
v2 = sorted(v2, reverse=True)
v3 = sorted(v3, reverse=True)

av0 = [0] + list(accumulate(v0))
av1 = [0] + list(accumulate(v1))
av2 = [0] + list(accumulate(v2))
av3 = [0] + list(accumulate(v3))

ans = 0
for i, j, k, l in product(range(len(v0) + 1), range(len(v1) + 1),
                          range(len(v2) + 1), range(len(v3) + 1)):
    v = av0[i] + av1[j] + av2[k] + av3[l]
    w = w0 * i + (w0 + 1) * j + (w0 + 2) * k + (w0 + 3) * l
    if w <= W:
        ans = max(v, ans)
print(ans)
