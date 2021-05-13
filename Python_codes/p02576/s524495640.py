##176
##A - Takoyaki
N,X,T = map(int,input().split())
a = 0
if N%X != 0:
    a = 1
print(int((N // X) * T + a * T))