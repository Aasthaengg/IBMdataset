from math import log2

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    X, Y = mi()
    cnt = 0
    while X <= Y:
        X *= 2
        cnt += 1
    print(cnt)
    


if __name__ == '__main__':
    main()
