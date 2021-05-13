n = int(input())
A = list(map(int, input().split()))

total = sum(A)
ans = 10**10
res = 0

for i in range(n-1):
    res += A[i]
    ans = min(ans, abs(total -2*res))

print(ans)
