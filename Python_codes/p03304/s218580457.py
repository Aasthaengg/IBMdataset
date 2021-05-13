N,M,D=map(int,input().split())
D=(N-D)*2-N*(D==0)
print(D*(M-1)/(N**2))