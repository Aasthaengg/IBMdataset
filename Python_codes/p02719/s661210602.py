n,k=map(int,input().split())
res=min(n%k,abs(n%k-k))
print(res)