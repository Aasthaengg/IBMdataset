N = int(input())
*A1, = map(int, input().split())
*A2, = map(int, input().split())
ans = 0
for i in range(N):
    ans = max(ans, sum(A1[:i+1]) + sum(A2[i:]))
print(ans)