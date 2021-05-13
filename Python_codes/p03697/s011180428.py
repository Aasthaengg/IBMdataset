def ABC_63_A():
    A,B = map(int, input().split())
    
    if A+B >= 10:
        print('error')
    else:
        print(A+B)

if __name__ == '__main__':

    ABC_63_A()