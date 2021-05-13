n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    j = 0
    if i < k:
        while i*(2**j) < k:
            j += 1
        ans += (1/n)*1/(2**j)
    else:
        ans += (1/n)
print(ans)