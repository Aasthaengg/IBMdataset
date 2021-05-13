A = input()
B = input()
C = input()

now = A[:1]
A = A[1:]

while(1):
    if(now == 'a'):
        if(len(A) == 0):
            print("A")
            exit()
        now = A[:1]
        A = A[1:]
    elif(now == 'b'):
        if(len(B) == 0):
            print("B")
            exit()
        now = B[:1]
        B = B[1:]
    else:
        if(len(C) == 0):
            print("C")
            exit()
        now = C[:1]
        C = C[1:]
