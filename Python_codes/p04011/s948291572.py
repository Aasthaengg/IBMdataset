N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = 0

for i in range(1,N+1):
    ans += X

if K < N:
    for i in range(1, N-K+1):
        ans += Y - X

print(ans)
