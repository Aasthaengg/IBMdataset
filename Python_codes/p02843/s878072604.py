X=int(input())
N=X//100
if N<0:
    print(0)
elif 100*N<=X<=105*N:
    print(1)
else:
    print(0)