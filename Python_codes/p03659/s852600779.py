N = int(input())
a = list(map(int, input().split()))
ans = float('inf')
l = 0
r = sum(a)

for i in range(N - 1):
    l += a[i]
    r -= a[i]
    ans = min(ans, abs(r - l))
    
print(ans)
