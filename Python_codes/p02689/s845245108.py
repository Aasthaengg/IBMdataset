N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
Ans = [True] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    Ha, Hb = H[a], H[b]
    if Ha <= Hb:
        Ans[a] = False
    if Ha >= Hb:
        Ans[b] = False
print(sum(Ans)-1)
