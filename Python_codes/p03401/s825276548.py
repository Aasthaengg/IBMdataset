import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    A = [0]+list(mi())+[0]
    S = sum(abs(A[i]-A[i+1]) for i in range(N+1))
    l = [S-abs(A[i]-A[i+1])-abs(A[i+1]-A[i+2])+abs(A[i]-A[i+2]) for i in range(N)]
    print(*l, sep='\n')


if __name__ == '__main__':
    main()
