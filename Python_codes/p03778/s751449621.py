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
    W, a, b = mi()
    if a+W < b:
        print(b-a-W)
    elif b+W < a:
        print(a-b-W)
    else:
        print(0)


if __name__ == '__main__':
    main()
