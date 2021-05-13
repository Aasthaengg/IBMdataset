n, m = map(int, input().split())
K = [0]*m
S = [[] for _ in range(m)]
for i in range(m):
    K[i], *S[i] = map(lambda x:int(x)-1, input().split())
    K[i] += 1
P = list(map(int, input().split()))

ans = 0
for i in range(pow(2,n)):
    B = bin(i)[2:].zfill(n)
    D = {j:True if b=='1' else False for j,b in enumerate(B)}
    _P = []
    for j,s in enumerate(S):
        _P.append(sum(D[_s] for _s in s)%2 == P[j])
    if all(_P):
        ans += 1
print(ans)