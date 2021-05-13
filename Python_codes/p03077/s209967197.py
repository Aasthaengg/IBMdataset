N=int(input())
A=[int(input()) for _ in range(5)]
M=min(A)
if N%M==0:
    print(4+N//M)
else:
    print(5+N//M)