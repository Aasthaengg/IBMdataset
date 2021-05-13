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
    N, A, B = mi()
    if (B-A)%2==0:
        print((B-A)//2)
    else:
        print(min(A+(B-A-1)//2, N-B+1+(B-A-1)//2))


if __name__ == '__main__':
    main()
