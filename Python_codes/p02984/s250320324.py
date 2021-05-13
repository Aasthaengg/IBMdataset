# D - Rain Flows into Dams

N = int(input())
A = [int(a) for a in input().split()]

x = 0
for i in range(N):
    x = 2 * A[i] - x

ans = [x // 2]
for i in range(N - 1):
    ans.append(2 * A[i] - ans[i])

print(*ans)
