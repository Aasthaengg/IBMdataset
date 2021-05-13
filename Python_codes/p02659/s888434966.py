A, B = input().split()
A = int(A)
B1 ,B2 = B.split('.') 
B1 = int(B1)
B2 = int(B2)
B1 = B1 *100 + B2
print((A*B1)//100)
