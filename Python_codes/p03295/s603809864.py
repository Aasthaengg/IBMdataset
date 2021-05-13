N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
AB.sort(key=lambda x: x[1])

ans = 1
t = AB[0][1]-1

for i in range(M):
    if t < AB[i][0]:
        t = AB[i][1]-1
        ans += 1
print(ans)
