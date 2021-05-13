n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    if (cnt + L[n-i-1][0]) % L[n-i-1][1]:
        cnt += L[n-i-1][1] - (cnt + L[n-i-1][0]) % L[n-i-1][1]
print(cnt)
