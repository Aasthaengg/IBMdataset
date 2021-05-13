import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    A,B = map(int,input().split())
    if A <= 8 and B <= 8:
        print('Yay!')
    else:
        print(':(')
if __name__ == '__main__':
    main()