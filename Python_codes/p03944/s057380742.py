import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    W,H,N = map(int,input().split())
    lx,rx,ly,ry = 0,W,0,H
    for _ in range(N):
        x,y,a = map(int,input().split())
        if a == 1:
            lx = max(lx,x)
        elif a == 2:
            rx = min(rx,x)
        elif a == 3:
            ly = max(ly,y)
        else:
            ry = min(ry,y)
    ans = max(0,rx - lx) * max(0,ry - ly)
    print(ans)
if __name__ == '__main__':
    main()