INF = 1000000000 + 7
N = int(input())
ans = 1
for i in range(1, N + 1):
    ans = ans * i % INF

print(ans)
