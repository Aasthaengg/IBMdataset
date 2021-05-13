N, M = list(map(int, input().split()))
L = [tuple(map(int, input().split())) for i in range(N)]
L.sort()
# print(L)
ct = 0
cost = 0
i = 0
while ct < M:
    a = min(M-ct, L[i][1])
    ct += a
    cost += a*L[i][0]
    # print(ct,cost)
    i += 1
print(cost)