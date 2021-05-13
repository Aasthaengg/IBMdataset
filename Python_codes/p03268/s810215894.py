n,k=map(int,input().split())
nki=n//k
ngu=(n*2)//k-nki
print(nki**3 if k%2 else nki**3+ngu**3)