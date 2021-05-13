n,k = map(int, input().split())
ans = 0
# a % b = k
for i in range(k+1,n+1):
    t = n // i
    s = max(n - (t*i + k) + (1 if k else 0),0)
    # print(s, t*i + k, n,  t*i)
    ans += t * (i-k) + s
print(ans)
