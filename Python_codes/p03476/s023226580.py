def Sieve_of_Eratosthenes(N,mode=False):
    """Nまでのエラトステネスの篩を実行

    N:自然数
    mode:False->素数のリスト,True->素数かどうかのリスト
    (False->[2,3,5,...],True->[False,False,True,True,False,True,...])
    """

    T=[True]*(N+1)
    T[0]=T[1]=0
    a=2
    while a*a<=N:
        if T[a]:
            b=a*a
            while b<=N:
                T[b]=False
                b+=a
        a+=1

    if mode:
        return T
    else:
        return [k for k in range(N+1) if T[k]]
#=====================================================
N_max=10**5
Q=int(input())

P=Sieve_of_Eratosthenes(N_max,True)
Y=[0]*(N_max+1)
for a in range(1,N_max+1):
    Y[a]=Y[a-1]+((a%2==1) and P[a] and P[(a+1)//2])

X=[0]*Q
for k in range(Q):
    l,r=map(int,input().split())
    X[k]=Y[r]-Y[l-1]

print("\n".join(map(str,X)))