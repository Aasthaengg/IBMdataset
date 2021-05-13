n,k=map(int,input().split())
A = list(map(int,input().split()))
n -= k
k -= 1
ans = 1
ans += (n+k-1)//k
print(ans)