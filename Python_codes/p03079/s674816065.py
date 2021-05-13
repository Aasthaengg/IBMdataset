if __name__=="__main__":
    A, B, C = input().split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    if A == B and B == C:
        print('Yes')
    else:
        print('No')