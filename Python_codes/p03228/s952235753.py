A,B,K=map(int,input().split())
for i in range(1,K+1):
    if i%2==1:
        if A%2==0:
            B=B+(A//2)
            A=A//2
        else:
            C=A-1
            B=B+(C//2)
            A=C//2
    elif i%2==0:
        if B%2==0:
            A=A+(B//2)
            B=B//2
        else:
            D=B-1
            A=A+(D//2)
            B=D//2
print(' '.join([str(A),str(B)]))