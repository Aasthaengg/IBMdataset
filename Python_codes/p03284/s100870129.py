n,k=map(int,input().split())
if n%k!=0:
    print(n//2+1-n//2)
else:
    print(0)