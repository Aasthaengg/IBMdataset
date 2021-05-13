import sys

A = input()
B = input()

if len(A)>len(B):
    print("GREATER")
elif len(A)<len(B):
    print("LESS")
else:
    for i in range(len(A)):
        if int(A[i])>int(B[i]):
            print("GREATER")
            sys.exit()
        elif int(A[i])<int(B[i]):
            print("LESS")
            sys.exit()
        else:
            continue
    else:
        print("EQUAL")