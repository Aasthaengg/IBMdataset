def ABC_120_A():
    A,B,C = map(int, input().split())
    if int(B/A) >= C:
        print(C)
    else:
        print(int(B/A))

if __name__ == '__main__':

    ABC_120_A()