A,B,C=map(int,input().split())
#Cの後は必ずB
if C<=B:
    print(B+C)
elif C<=(A+B):
    print(B+C)
else:
    print(A+2*B+1)