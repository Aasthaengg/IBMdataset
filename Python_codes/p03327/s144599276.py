import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    if N < 1000:
        print('ABC')
    else:
        print('ABD')

if __name__ == '__main__':
    main()