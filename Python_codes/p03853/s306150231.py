import sys
sys.setrecursionlimit(500000)
MOD = 10**9+7

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
    H, W = mi()
    C = [input() for i in range(H)]
    for i in range(H):
        print(C[i], C[i], sep='\n')


if __name__ == '__main__':
    main()
