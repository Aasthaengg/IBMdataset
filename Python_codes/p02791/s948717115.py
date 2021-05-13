N = int(input())
P = list(map(int, input().split()))

minP = 0
ans = 0
for i in range(N):
    if i == 0:
        ans += 1
        minP = P[0]
        continue
    if minP >= P[i]:
        ans += 1
        minP = P[i]
print(ans)
