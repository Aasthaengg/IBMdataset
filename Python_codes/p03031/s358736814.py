from itertools import product

n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

cnt = 0
for pat in product([0, 1], repeat=n):
    for i, ksi in enumerate(ks):
        tmp = sum(pat[ksi[j + 1] - 1] for j in range(ksi[0]))
        if  tmp % 2 != p[i]:
            break
    else:
        cnt += 1
print(cnt)
