N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

A.sort(key=lambda x:x[1])

ans = 1
end = A[0][1]
for i in range(1,M):
    if A[i][0]>=end:
        ans += 1
        end = A[i][1]
print(ans)