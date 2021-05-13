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
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] == 'A':
            break
    for j in range(n-1, -1, -1):
        if s[j] == 'Z':
            break
    print(j-i+1)


if __name__ == '__main__':
    main()
