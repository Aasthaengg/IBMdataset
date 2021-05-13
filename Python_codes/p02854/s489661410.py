N = int(input())
A = list(map(int,input().split()))
ans = 10**18
left = 0
right = sum(A)
for i in range(N):
    ans = min(ans, abs(left-right))
    left += A[i]
    right -= A[i]
print(ans)