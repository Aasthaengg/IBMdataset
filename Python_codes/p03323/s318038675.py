def ABC_100_A():
    A,B = map(int, input().split())
    
    if A <= 8 and B <= 8:
        print('Yay!')
    else:
        print(':(')

if __name__ == '__main__':

    ABC_100_A()