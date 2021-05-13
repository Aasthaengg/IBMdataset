import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def Base(X, n):
    if (int(X/n)):
        return Base(int(X/n), n)+str(X%n)
    return str(X%n)

def main():
    N = ii()
    m = 10**100
    for i in range(N+1):
        a = sum(map(int, Base(i, 6)))
        b = sum(map(int, Base(N-i, 9)))
        m = min(m, a+b)
    print(m)

if __name__ == '__main__':
    main()
