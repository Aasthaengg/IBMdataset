N, M = map(int, input().split())
A = list(map(int, input().split()))
d = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
D = {a: d[a] for a in A}
m = min(D.values())
E = {}
for k, v in D.items():
    v -= m
    if v in E:
        E[v] = max(E[v], k)
    else:
        E[v] = k
F = sorted(E.keys(), key=lambda f: (max(0, E[f]-E[0]), f), reverse=True)
F.remove(0)
K = N // m
for k in range(K, 0, -1):
    B = [E[0]] * k
    R = N - k * m
    if not R:
        print("".join(map(str, sorted(B, reverse=True))))
        break
    def rec(r, i, j):
        if i < 0:
            return
        for f in F[j:]:
            if r == f:
                B[i] = E[f]
                print("".join(map(str, sorted(B, reverse=True))))
                exit()
            elif r > f:
                B[i], tmp = E[f], B[i]
                rec(r - f, i - 1, j)
                B[i] = tmp
            j += 1
    rec(R, k-1, 0)