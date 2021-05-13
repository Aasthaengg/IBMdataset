N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

res = [[0]*N for _ in range(2)]
res[0][0] = A1[0]
res[1][N-1] = A2[N-1]

for i in range(1, N):
    res[0][i] = res[0][i-1]+A1[i]
    res[1][N-i-1] = res[1][N-i]+A2[N-i-1]

r = 0
for i in range(N):
    r = max(res[0][i]+res[1][i], r)

print(r)