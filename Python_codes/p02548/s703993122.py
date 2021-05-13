N = int(input())
nd = [0] * (N+1)
for i in range(1, N):
    for j in range(i, N, i):
        nd[j] += 1
print(sum(nd))