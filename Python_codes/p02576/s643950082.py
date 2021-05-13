N,X,T=map(int,input().split())
N=((N//X)+1 if N%X else N//X)
print(N*T)