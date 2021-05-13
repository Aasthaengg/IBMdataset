n,k=map(int,input().split())

m=n//k
print(min(n-(m-1)*k, n-m*k, (m+1)*k-n))