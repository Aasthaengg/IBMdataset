n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    p = 1
    j = 0
    while i*pow(2,j) < k:
        j += 1
    ans += pow(0.5,j)/n
print(ans)