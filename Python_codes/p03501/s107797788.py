def ABC_80_A():
    N,A,B = map(int, input().split())
    
    if A*N <= B:
        print(A*N)
    else:
        print(B)

if __name__ == '__main__':

    ABC_80_A()