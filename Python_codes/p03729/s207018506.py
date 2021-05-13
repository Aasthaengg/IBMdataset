A,B,C=input().split()
A=str(A)
B=str(B)
c=str(C)
if (A[-1]==B[0]) and (B[-1] == c[0]):
    print ("YES")
else:
    print ("NO")
