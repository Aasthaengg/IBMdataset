def ABC_94_A():
    A,B,X = map(int, input().split())
    
    if A+B>=X and A<=X:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':

    ABC_94_A()