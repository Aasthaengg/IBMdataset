import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    k = NI()

    a = k // 50
    p = [49+a] * 50
    b = k % 50

    for i in range(b):
        for j in range(50):
            if i == j:
                p[j] += 50
            else:
                p[j] -= 1


    print(50)
    print(*p,sep=' ')



if __name__ == '__main__':
    main()