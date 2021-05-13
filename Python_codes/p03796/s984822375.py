n = int(input())
ans = 1
p = pow(10,9)+7
for i in range(2,n+1):
    ans = (i * ans)%p
print(ans)