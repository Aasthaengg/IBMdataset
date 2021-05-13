import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = int(readline())
    B = int(readline())
    
    if A > B:
        A,B= B, A
    
    if A == 1:
        if B == 2:
            print('3')
        else:
            print('2')
    else:
        print('1')
    
    return


if __name__ == '__main__':
    main()
