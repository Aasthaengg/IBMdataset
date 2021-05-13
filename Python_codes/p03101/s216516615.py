import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    H,W=map(int,input().split())
    h,w=map(int,input().split())
    print(H*W-h*W-H*w+h*w)

if __name__ == '__main__':
    main()