
if __name__ == '__main__':
    # ??????????????\???
    S_size = int(input())
    S = set([int(x) for x in input().split(' ')])
    T_size = int(input())
    T = set([int(x) for x in input().split(' ')])
    # S = [1, 2, 3, 4, 5, 1]
    # T = set([3, 4, 1])

    # ????????????
    U = S.intersection(T)

    # ???????????????
    print('{0}'.format(len(U)))