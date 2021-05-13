N = int(input())
if N==0:
    print(0)
else:
    A = []
    while N!=0:
        if N%2==1:
            A.append("1")
            N -= 1
        else:
            A.append("0")
        N = N//(-2)
    A = A[::-1]
    print("".join(A))