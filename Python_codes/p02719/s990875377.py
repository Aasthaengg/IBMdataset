n,k=map(int,input().split())

print(min(n-k*(n//k),-n+k*(n//k+1)))
