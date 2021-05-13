import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    t,x=map(int,input().split())
    print(t/x)

if __name__ == '__main__':
    main()
