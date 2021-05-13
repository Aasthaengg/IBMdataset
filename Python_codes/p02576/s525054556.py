N,X,T = map(int,input().split())
P = int(N/X)
Z = T*P
if N%X == 0:
    print(Z)
else:
    print(int(Z+T))	