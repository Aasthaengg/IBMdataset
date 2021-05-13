n,k = map(int,input().split())
x = (n-k) * 100
ans = (x + k*1900)* 2**k
print(ans)