n, k = map(int, input().split())
ans = 0
for i in range(k+1, n+1):
    ans += (n//i * (i-k))
    val = n % i
    #print(ans)

    ans += max(0, val - max(0,(k-1)))
    #print(ans)
print(ans)
