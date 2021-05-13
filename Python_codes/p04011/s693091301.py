#高橋君とホテルイージー
def ABC_44_A():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    syukuhakuhi = 0

    for i in range(N+1):

        if i!=0:
            if i <= K:
                syukuhakuhi+=X
            else:
                syukuhakuhi+=Y
    print(syukuhakuhi)


if __name__ == '__main__':

    ABC_44_A()