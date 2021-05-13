N, dT = map(int, input().split())
T = list(map(int, input().split())) + [float('inf')]
ans = 0
for i in range(N):
    ans += min(dT, T[i+1] - T[i])
print(ans)
