def ALDS1_4A():
    n, S = int(input()), set(map(int, input().split()))
    q, T = int(input()), set(map(int, input().split()))
    print(len(S.intersection(T)))
if __name__ == '__main__':
    ALDS1_4A()