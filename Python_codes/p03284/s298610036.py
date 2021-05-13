import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N,K = map(int,input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)    
if __name__ == '__main__':
    main()