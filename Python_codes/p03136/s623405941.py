import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')


def main():
    N = int(readline())
    L = list(map(int, readline().split()))

    if sum(L)-max(L)>max(L):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
