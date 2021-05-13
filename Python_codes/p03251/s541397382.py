MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n,m,x,y = map(int,input().split())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    t = max(X)
    s = min(Y)
    if max(t,x) < min(s,y):
        print('No War')
    else:
        print('War')
if __name__ == '__main__':
    main()