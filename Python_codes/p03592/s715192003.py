n,m,k = [int(x) for x in input().split()]

ans = "No"
for i in range(n+1):
    for j in range(m+1):
        if i * (m-j) + j * (n-i) == k:
            ans = "Yes"
            break

print(ans)