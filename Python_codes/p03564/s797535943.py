n = int(input())
k = int(input())
ans = 2**n
for i in range(n+1):
    tmp = 2**i + k*(n-i)
    ans = min(ans,tmp)
print(ans)
