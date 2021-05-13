def ABC_118_A():
    A,B = map(int, input().split())
    if B%A == 0:
        print(A+B)
    else:
        print(B-A)

if __name__ == '__main__':

    ABC_118_A()