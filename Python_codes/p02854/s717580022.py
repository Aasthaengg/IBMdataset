N = int(input())
A = list(map(int, input().split()))
ans = float('inf')
l_sum = 0
r_sum = sum(A)
for i in range(N):
    l_sum += A[i]
    r_sum -= A[i]
    ans = min(ans, abs(r_sum - l_sum))

print(ans)