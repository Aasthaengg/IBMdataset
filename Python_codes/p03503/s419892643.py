import itertools

n = int(input())
F = [None for i in range(n)]
P = [None for i in range(n)]
for i in range(n):
    F[i] = list(map(int, input().split()))
for i in range(n):
    P[i] = list(map(int, input().split()))
comb = list(itertools.product([0,1],repeat=10))
comb.pop(0)
# print(F)
# print(P)
# print(comb)

ans = -float("INF")
for i in comb:
    koho = 0
    for j in range(n):
        count = 0
        for k in range(10):
            if i[k]==1 and F[j][k]==1:
                count+=1
        koho += P[j][count]
    ans = max(ans,koho)

print(ans)
