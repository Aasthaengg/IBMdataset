N = int(input())

ans = 0
for i in range(1, N):
    sho = (N - 1) // i
    ans += sho

print(ans)
