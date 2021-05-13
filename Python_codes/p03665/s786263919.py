N,P=map(int,input().split())
*A,=map(int,input().split())

B=[a%2 for a in A]
if sum(B)==0:
    print((P==0)*2**N)
else:
    print(2**(N-1))