def ABC_143_A():
    A,B = map(int, input().split())
    if A - 2*B >= 0:
        print(A-2*B)
    else:
        print(0)


if __name__ == '__main__':

    ABC_143_A()