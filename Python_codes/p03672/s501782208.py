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
    S = input()
    N = len(S)//2
    for i in range(1, N+1):
        t = S[:2*N-2*i]
        n = len(t)//2
        if t[:n] == t[n:]:
            print(2*n)
            return

if __name__ == '__main__':
    main()
