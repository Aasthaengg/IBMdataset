A,B,C=map(int,input().split())
D=int(A-B)
if A==B:
    print(C)
elif C-D<=0:
    print(0)
else:
    print(C-D)
