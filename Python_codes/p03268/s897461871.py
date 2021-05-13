n,k=map(int,input().split())
print((n//k)**3 if k%2==1 else (n//k)**3+((n+k//2)//k)**3)
