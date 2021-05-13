n = int(input())
A = list(map(int, input().split()))
s = sum(A)
l = 0
ans = 10**18
for i in range(n-1):
    l += A[i]
    r = s-l
    ans = min(ans, abs(l-r))
print(ans)
