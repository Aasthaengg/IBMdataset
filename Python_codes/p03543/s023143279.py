def ABC_79_A():
    N = input()
    
    if N.count(N[0]) == 4:
        print('Yes')
    elif (N[0] == N[1] and N[1] == N[2]) or (N[1] == N[2] and N[2] == N[3]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':

    ABC_79_A()