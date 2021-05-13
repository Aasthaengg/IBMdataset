import sys
sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N = ii()
    T = list(mi())
    M = ii()
    P, X = i2(M)

    S = sum(T)
    for i in range(M):
        print(S-T[P[i]-1]+X[i])


if __name__ == '__main__':
    main()
