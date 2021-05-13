N=sorted(list(map(int,input().split())))
A=N[0]
B=N[1]
if A==B:
    print(A+B)
else:
    print(B+B-1)