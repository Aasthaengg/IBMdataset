A = list(input())
B = list(input())
C = list(input())
n = A[0]
del A[0]
while True:
    if n == "a":
        if A == []:
            print("A")
            break
        n = A[0]
        del A[0]
    elif n == "b":
        if B == []:
            print("B")
            break
        n = B[0]
        del B[0]
    else:
        if C == []:
            print("C")
            break
        n = C[0]
        del C[0]
        
