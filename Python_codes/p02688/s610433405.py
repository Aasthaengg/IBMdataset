N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))


count = [0] * N
for i in range(K):
    for j in range(d[i]):
        count[A[i][j]-1] += 1

ans = count.count(0)
print(ans)