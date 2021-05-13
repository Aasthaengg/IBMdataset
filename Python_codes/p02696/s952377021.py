A,B,N=map(int,input().split())

f=lambda x: (A*x)//B+A*(x//B)

if B>N:
    print(f(N))
else:
    print(f(B-1))
