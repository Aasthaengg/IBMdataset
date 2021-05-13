def ABC_65_A():
    X,A,B = map(int, input().split())
    
    if A >= B:
        print('delicious')
    elif A+X >= B:
        print('safe')
    else:
        print('dangerous')

if __name__ == '__main__':

    ABC_65_A()