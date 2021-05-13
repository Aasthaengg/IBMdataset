#Addition and Subtraction Easy
def ABC_50_A():
    A,B,C = map(str, input().split())

    if B[0] == '+':
        print(int(A)+int(C))
    else:
        print(int(A)-int(C))


if __name__ == '__main__':

    ABC_50_A()