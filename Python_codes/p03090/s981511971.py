def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    print(N*(N-1)//2-N//2)
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j == N - N % 2 - (i - 1):
                continue
            print(i, j)

if __name__ == '__main__':
    main()


'''
4:
 1 [ , 2, 3,  ] = 9
 2 [1,  ,  , 4] = 8
 3 [1,  ,  , 4] = 7
 4 [ , 2, 3,  ] = 6
5:
 1 [ , 2, 3,  , 5] = 10
 2 [1,  ,  , 4, 5] = 10
 3 [1,  ,  , 4, 5] = 10
 4 [ , 2, 3,  , 5] = 10
 5 [1, 2, 3, 4, ] = 10
6:
 1 [   2, 3, 4, 5,  ] = 14
 2 [1,    3, 4,  , 6] = 14
 3 [1, 2,    4, 5, 6] = 18
 4 [1, 2, 3,    5, 6] = 17
 5 [1,  , 3, 4,    6] = 14
 6 [ , 2, 3, 4, 5,  ] = 14
'''