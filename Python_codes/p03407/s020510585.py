def ABC_91_A():
    A,B,C = map(int, input().split())
    
    if A+B>=C:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    ABC_91_A()