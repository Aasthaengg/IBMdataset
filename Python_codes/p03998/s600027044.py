A = list(input())
B = list(input())
C = list(input())
turn = 1
for i in range(len(A)*3):
    if turn == 1:
        #A勝利
        if len(A) == 0:
            print("A")
            break
        else:
            if A[0] == "a":
                turn = 1
            elif A[0] == "b":
                turn = 2
            elif A[0] == "c":
                turn = 3
            A.remove(A[0])
    if turn == 2:
        #B勝利
        if len(B) == 0:
            print("B")
            break
        else:
            if B[0] == "a":
                turn = 1
            elif B[0] == "b":
                turn = 2
            elif B[0] == "c":
                turn = 3
            B.remove(B[0])
    if turn == 3:
        #C勝利
        if len(C) == 0:
            print("C")
            break
        else:
            if C[0] == "a":
                turn = 1
            elif C[0] == "b":
                turn = 2
            elif C[0] == "c":
                turn = 3
            C.remove(C[0])