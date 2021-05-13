H, W = map(int, input().split())
INF = 10**15
c = []
for i in range(10):
    tmp = list(map(int, input().split()))
    c.append(tmp)

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k]+c[k][j])
count = [0]*10
for i in range(H):
    tmp = list(map(int, input().split()))
    for t in tmp:
        if t != -1:
            count[t] += 1

ans = 0
for i in range(10):
    ans += count[i] * c[i][1]

print(ans)
    
