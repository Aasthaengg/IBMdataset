#HonestOrDishonest
def ABC_56_A():
    A,B = map(str, input().split())
    
    if A == 'H' and B == 'H':
        print('H')
    elif A == 'H' and B == 'D':
        print('D')
    elif A == 'D' and B == 'H':
        print('D')
    else:
        print('H')

if __name__ == '__main__':

    ABC_56_A()