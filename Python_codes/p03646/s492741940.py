K = int(input())

N = 50
res = [i for i in range(N)]
for i in range(K % N):
    for j in range(N):
        if i == j:
            res[j] += N
        else:
            res[j] -= 1
for j in range(N):
    res[j] += K // N

print(N)
print(" ".join([str(n) for n in res]))
