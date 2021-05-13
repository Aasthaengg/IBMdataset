n, K = map(int, input().split())
As = list(map(int, input().split()))

# doubling
m = 0
while 2**m < K:
    m += 1
d = [[0] * n for i in range(m)]
for i in range(n):
    d[0][i] = As[i] - 1 

for k in range(m-1):
    for i in range(n):
        d[k+1][i] = d[k][d[k][i]]

now = 0
for k in range(m):
    if (K >> k) & 1:
        now = d[k][now]

print(now+1)
