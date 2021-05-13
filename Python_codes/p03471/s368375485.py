N,Y=input().split()
N=int(N)
Y=int(Y)
def roop():
    for a in range(N+1):
        a_amount=10000*a
        for b in range(N+1-a):
            b_amount=5000*b
            c=N-a-b
            c_amount=1000*c
            amount_tot=a_amount+b_amount+c_amount
            X=[a,b,c]
            if Y==amount_tot and a+b+c==N:
                return X
    return -1,-1,-1
roop()
ans=roop()
print(' '.join(map(str,ans)))