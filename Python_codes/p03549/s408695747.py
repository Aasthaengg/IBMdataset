import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]

    print((100 * (N - M) + 1900 * M) * (2 ** M))

    
    

if __name__ == '__main__':
    main()

