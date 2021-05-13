#AtCoDeerくんとペンキ
def ABC_46_A():
    A,B,C = map(int, input().split())
    iroha = [0 for i in range(3)]
    iroha = []
    iroha.append(A)
    iroha.append(B)
    iroha.append(C)

    if iroha.count(A)==3:
        print(1)
    elif iroha.count(A)==2 or iroha.count(B)==2:
        print(2)
    else:
        print(3)

if __name__ == '__main__':

    ABC_46_A()