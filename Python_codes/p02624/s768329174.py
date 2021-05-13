n = int(input())
lis = [0]*(n+1)
for i in range(2,n+1):
    j = 1
    while i*j <= n:
        lis[i*j] += 1
        j += 1
ans = 0
for i in range(2,n+1):
    ans += (lis[i]+1)*i
print(ans+1)