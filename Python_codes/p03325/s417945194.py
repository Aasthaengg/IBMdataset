# coding=utf-8

if __name__ == '__main__':
    N = int(input())
    lia = list(map(int, input().split()))

    C = 0
    for i in range(N):
        if lia[i] % 2 ==0:
            tmp = lia[i]
            while tmp % 2 ==0:
                tmp = tmp / 2
                C += 1

    print(int(C))