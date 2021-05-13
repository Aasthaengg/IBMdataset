A,B=map(int,input().split())
if (2*A-1)>=(2*B-1) and (2*A-1)>=(A+B):
    print(2*A-1)
elif (2*B-1)>=(2*A-1) and (2*B-1)>=(A+B):
    print(2*B-1)
elif (A+B)>=(2*A-1) and (A+B)>=(2*B-1):
    print(A+B)