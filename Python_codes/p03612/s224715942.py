N = int(input())
P = list(map(int, input().split()))

ans = 0

for i in range(N):
    if P[i] != i+1:
        continue
    if i+1 < N and P[i] != i+2 or i == 0:
        P[i], P[i+1] = P[i+1], P[i]
        ans += 1
    else:
        P[i], P[i-1] = P[i-1], P[i]
        ans += 1

print(ans)
