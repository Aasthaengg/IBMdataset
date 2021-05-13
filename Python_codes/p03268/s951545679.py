n,k=map(int,input().split())
print((n//k)**3+((n+k//2)//k)**3*(1-k%2))