def ABC_135_A():
    A,B = map(int, input().split())

    if (A+B)%2 == 0:
        print(int((A+B)/2))
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':

    ABC_135_A()