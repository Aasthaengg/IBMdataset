#キャンディーと２人の子供
def ABC_47_A():
    A,B,C = map(int, input().split())

    if A > B and A > C:
        if A == B + C:
            print('Yes')
        else:
            print('No')
    elif B > A and B > C:
        if B == A + C:
            print('Yes')
        else:
            print('No')
    else:
        if C == A + B:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':

    ABC_47_A()