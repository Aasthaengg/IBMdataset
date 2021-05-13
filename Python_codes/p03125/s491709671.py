import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    A,B=map(int,input().split())
    if B%A==0:
        print(A+B)
    else:
        print(B-A)

if __name__ == '__main__':
    main()
