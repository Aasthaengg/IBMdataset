n,m,k = map(int,input().split())
ans = 0
for i in range(n+1):
    for j in range(m+1):
        a = i*m + j*n - 2*i*j
        if a == k:
            ans = 1
            break
print(["No","Yes"][ans])