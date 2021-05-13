N = int(input())
A = list(map(int, input().split()))

s = [0]*(N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]

ans = float('inf')
for i in range(1,N):
    ans = min(abs(s[N]-s[i]-s[i]),ans)
print(ans)