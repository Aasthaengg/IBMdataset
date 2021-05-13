import math
A,B=input().split()
A=int(A)
B,C=B.split('.')
B=int(B)
C=int(C)
print(A*(B*100+C)//100)