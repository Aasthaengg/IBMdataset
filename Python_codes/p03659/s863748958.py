n = int(input())
a = list(map(int, input().split()))

total = sum(a)
s = 0
ans = 10**9 * 2 * 10**5
for i in range(0, n-1):
    s += a[i]
    ans = min(ans, abs(s - (total-s)))
    
print(ans)
