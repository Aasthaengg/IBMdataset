N = int(input())

ans = 0

for n in range(1, N+1, 2):
        ans += len([i for i in range(1, n+1) if n%i == 0]) == 8

print(ans)