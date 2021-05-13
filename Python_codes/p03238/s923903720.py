import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    if N==1:
        print('Hello World')
    else:
        A=int(input())
        B=int(input())
        print(A+B)

if __name__ == '__main__':
    main()
