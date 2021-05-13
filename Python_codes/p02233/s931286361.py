n=int(input())
if n==0 or n==1:
    print(1)
else:
    N=1
    m=1
    for i in range(n-1):
        M=N+m
        m=N
        N=M
    print(M)
