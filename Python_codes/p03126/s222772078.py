n, m = map(int, input().split())
suki = [0]*(m+1)

for i in range(n):
    ka = list(map(int, input().split()))
    for j in range(1, ka[0]+1):
        suki[ka[j]] += 1

ans = 0
for i in range(1, m+1):
    if suki[i] == n:
        ans += 1
print(ans)
