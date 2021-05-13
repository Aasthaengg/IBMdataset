def ABC_67_A():
    A,B = map(int, input().split())
    
    if A%3 == 0:
        print('Possible')
    elif B%3 == 0:
        print('Possible')
    elif (A+B)%3 == 0:
        print('Possible')
    else:
        print('Impossible')

if __name__ == '__main__':

    ABC_67_A()