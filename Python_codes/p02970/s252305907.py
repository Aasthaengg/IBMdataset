N,D=map(int,input().split())

D=1+D+D

if N%D==0:
    print(int(N/D))

else:
    print(int(N/D)+1)
