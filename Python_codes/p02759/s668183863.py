N=input()
N=int(N)

if N%2==1:
    N=int(((N-1)/2)+1)
    print(N)
else:
    N=int(N/2)
    print(N)