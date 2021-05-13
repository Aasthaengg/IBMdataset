N=int(input())
if N%111==0:
    print(N)
else:   
    A=(N//111+1)*111
    print(A)