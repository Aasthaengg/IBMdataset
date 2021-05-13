def ABC_124_A():
    A,B = map(int, input().split())
    print(max(A+A-1,A+B,B+B-1))


if __name__ == '__main__':

    ABC_124_A()