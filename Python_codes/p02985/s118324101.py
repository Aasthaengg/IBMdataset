from itertools import groupby

[N, K] = map(int, input().split())

num_of_perms = [1] * (K-1)
for i in range(1, K-1):
    num_of_perms[i] = num_of_perms[i-1] * ((K - 2) - i + 1) % 1000000007

Es = []
for _ in range(0, N-1):
    [a, b] = input().split()
    Es.append(int(a))
    Es.append(int(b))

if N == 1:
    res = K
else:
    res = K * (K-1)
    res %= 1000000007
    for g in groupby(sorted(Es)):
        c = len(list(g[1]))
        if c > K-1:
            res = 0
            break
        res *= num_of_perms[c-1]
        res %= 1000000007

print(res)
