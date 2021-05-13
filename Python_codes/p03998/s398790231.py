def abc045_b():
    A,B,C = [input() for i in range(3)] #入力
    A = list(A)
    B = list(B)
    C = list(C)
    D = len(A) + len(B) + len(C)
    Var = A[0] #Aスタート
    for d in range(D):
        if Var == 'a' and len(A) == 0:
            print('A')
            break
        elif Var == 'a':
            Var = A[0]
            del A[0]
        elif Var == 'b' and len(B) == 0:
            print('B')
            break
        elif Var == 'b':
            Var = B[0]
            del B[0]
        elif Var == 'c' and len(C) == 0:
            print('C')
            break
        elif Var == 'c':
            Var = C[0]
            del C[0]
if __name__ == '__main__':
    abc045_b()