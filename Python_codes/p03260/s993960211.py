def ABC_109_A():
    A,B = map(int, input().split())

    if A%2 != 0 and B%2 != 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    ABC_109_A()