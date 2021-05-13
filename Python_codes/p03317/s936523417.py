n,k = map(int,input().split())
a = list(map(int,input().split()))
n-=1
k-=1
if n%k==0: print(n//k)
else: print(n//k+1)