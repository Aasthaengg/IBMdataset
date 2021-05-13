import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())


def main():
    N = ii()
    A = list(mi())
    B = [0]*N
    B[0] = sum(A[i]*((-1)**(i%2)) for i in range(N))
    for i in range(1, N):
        B[i] = 2*A[i-1]-B[i-1]
    print(*B)


if __name__ == '__main__':
    main()
