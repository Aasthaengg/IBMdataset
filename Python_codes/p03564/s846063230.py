N = int(input())
K = int(input())
ans = 10**9
for i in range(N+1):
    ans = min(2**i+K*(N-i),ans)
print(ans)
