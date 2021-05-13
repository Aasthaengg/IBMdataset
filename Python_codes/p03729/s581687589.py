#Shiritori
def ABC_60_A():
    A,B,C = map(str, input().split())
    
    if A[len(A)-1] == B[0] and B[len(B)-1] == C[0]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':

    ABC_60_A()