N,X,T=map(int,input().split())

c=0
while N>0:  
    N=N-X
    c+=T
print(c)