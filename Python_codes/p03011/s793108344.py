def ABC_129_A():
    P,Q,R = map(int, input().split())
    print(min(P+Q,Q+R,R+P))


if __name__ == '__main__':

    ABC_129_A()