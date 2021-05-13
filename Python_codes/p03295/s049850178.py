N, M = map(int, input().split())

AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))
AB = sorted(AB, key=lambda x: x[1])

ans = 1
D = AB[0][1]
for i in range(1, M):
    if AB[i][0] >= D:
        ans += 1
        D = AB[i][1]
print(ans)
