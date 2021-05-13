def q1():
    K, X = (int(i) for i in input().split())
    if K * 500 >= X:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    q1()
