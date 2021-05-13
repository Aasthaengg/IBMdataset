N = int(input())
*A, = map(int, input().split())
ac = [0]*(N+1)
for i in range(1, N+1):
    ac[i] = ac[i-1]+A[i-1]
ans = float("inf")
for i in range(1, N):
    ans = min(ans, abs(ac[i]-(ac[N]-ac[i])))
print(ans)
