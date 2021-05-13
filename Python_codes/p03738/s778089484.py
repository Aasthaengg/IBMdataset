A = input()
B = input()
if len(A) > len(B):
    print("GREATER")
elif len(A) < len(B):
    print("LESS")
else:
    for k in range(len(A)):
        if int(A[k]) > int(B[k]):
            print("GREATER")
            exit(0)
        elif int(A[k]) < int(B[k]):
            print("LESS")
            exit(0)
    print("EQUAL")
