import math

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, K = mi()
    l = list(mi())
    l.sort(reverse=True)
    print(sum(l[:K]))

if __name__ == '__main__':
    main()