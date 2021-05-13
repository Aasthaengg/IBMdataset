import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    K, X =map(int,input().split())

    for i in range(2*K-1):
        print(X-K+1+i,end =" ")


if __name__ == "__main__":
    main()
