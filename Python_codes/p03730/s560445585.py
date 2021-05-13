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
    A, B, C = mi()
    for i in range(B):
        if (A*i)%B == C:
            print('YES')
            return
    print('NO')

if __name__ == '__main__':
    main()
