N = int(input())
A = list(map(int, input().split()))

X = sum(A)
x = 0
ans = 10000000000007

for i in range(N):
    x += A[i]
    if i+1<N : ans=min(ans,abs(2*x-X))

print(ans)
