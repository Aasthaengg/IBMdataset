def ABC_71_A():
    X,A,B = map(int, input().split())
    
    if abs(X-A) <= abs(X-B):
        print('A')
    else:
        print('B')

if __name__ == '__main__':

    ABC_71_A()