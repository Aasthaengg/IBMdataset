import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,i=map(int,input().split())
    print(N-i+1)

if __name__ == '__main__':
    main()
