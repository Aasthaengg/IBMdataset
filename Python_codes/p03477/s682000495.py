def ABC_83_A():
    A,B,C,D = map(int, input().split())
    
    if A+B>C+D:
        print('Left')
    elif A+B==C+D:
        print('Balanced')
    else:
        print('Right')

if __name__ == '__main__':

    ABC_83_A()