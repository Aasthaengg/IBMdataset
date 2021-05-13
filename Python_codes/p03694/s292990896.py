import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())


def main():
    N = ii()
    a = list(mi())
    print(max(a)-min(a))



if __name__ == '__main__':
    main()
