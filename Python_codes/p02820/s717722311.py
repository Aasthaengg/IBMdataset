N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()


ok = [True] * N
d = {"r": P, "s": R, "p": S}
ans = 0
for i in range(N):
    if i >= K and T[i - K] == T[i] and ok[i - K]:
        ok[i] = False
    if ok[i]:
        ans += d[T[i]]
print(ans)
