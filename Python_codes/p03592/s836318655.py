n,m,k = map(int, input().split())
ans = "No"
for i in range(n+1):
    for j in range(m+1):
        l = i*(m-j) + (n-i)*j
        if k==l:
            ans ="Yes"
        else:
            continue
print(ans)