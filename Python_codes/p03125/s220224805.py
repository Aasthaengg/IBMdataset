A,B=input().split()
A=int(A)
B=int(B)
print((B%A==0)*(A+B)+(B%A!=0)*(B-A))