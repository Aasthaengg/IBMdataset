import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, M = mi()
    if N == M == 1:
        print(1)
    elif N == 1 or M == 1:
        print(max(N, M)-2)
    else:
        print((N-2)*(M-2))


if __name__ == '__main__':
    main()
