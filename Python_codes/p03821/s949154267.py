N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    ans += (A[i][1] - (A[i][0]+ans) % A[i][1]) % A[i][1]
print(ans)
