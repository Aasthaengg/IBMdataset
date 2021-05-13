n,k = map(int,input().split())
h = list(map(int,input().split()))
ans = sum(h[i] >= k for i in range(n))
print(ans)
