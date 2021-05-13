def ABC_72_A():
    X,t = map(int, input().split())
    
    if X-t >=0:
        print(X-t)
    else:
        print(0)

if __name__ == '__main__':

    ABC_72_A()