N = int(input())

S = []
for _ in range(N):
    s = int(''.join(input().split()), 2)
    S.append(s)

P = []
for _ in range(N):
    p = [int(i) for i in input().split()]
    P.append(p)

ans = -10**20
for i in range(1, 2 ** 10):
    c = 0
    for j in range(N):
        c += P[j][bin(S[j] & i).count('1')]
    ans = max(ans, c)

print(ans)
