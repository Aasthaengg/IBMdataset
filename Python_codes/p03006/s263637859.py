n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(1)
    exit()
    
pq = []
for i in range(n):
    for j in range(n):
        if i != j:
            pq.append((xy[i][0] - xy[j][0] ,xy[i][1] - xy[j][1]))

ans = float("inf")
for p, q in pq:
    tmp = 0
    for i in range(n):
        for j in range(n):
            if i != j and (p, q) == (xy[i][0] - xy[j][0] ,xy[i][1] - xy[j][1]):
                tmp += 1
        ans = min(ans, n - tmp)
            
print(ans)