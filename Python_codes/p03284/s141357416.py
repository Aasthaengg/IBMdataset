def ABC_105_A():
    N,K = map(int, input().split())
    
    if N%K == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':

    ABC_105_A()