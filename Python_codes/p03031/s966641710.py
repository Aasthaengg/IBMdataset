
N, M = map(int, input().split())
K = []
X = []
for _ in range(M):
    k, *x = list(map(int, input().split()))
    K.append(k)
    X.append(x)
P = list(map(int, input().split()))

ans = 0
for bit in range(2 ** N):
    light_on = [False] * M
    for i in range(M):
        tmp = 0
        for s in X[i]:
            tmp += bit >> (s - 1) & 1
        light_on[i] = tmp % 2 == P[i]

    ans += all(light_on)

print(ans)
