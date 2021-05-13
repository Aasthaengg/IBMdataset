#Sharing Cookies
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

#ABCxxx
def ABC_68_A():
    N = input()
    print('ABC'+N)
    
    

if __name__ == '__main__':

    ABC_67_A()