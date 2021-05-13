n,k=list(map(int,input().split()))
md = n%k
print(min(md,k-md))
