K = int(input())

N = 50
res = [i - K for i in range(N)]
p,q = divmod(K, N)
for i in range(N):
    if i < q:
        res[i] += (p + 1) * (N + 1)
    else:
        res[i] += p * (N + 1)
print(N)
print(*res)