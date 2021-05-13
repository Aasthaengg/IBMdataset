import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    M=10**9
    S=I()
    if S<=M:
        print(0,0,0,S,1,0)
    else:
        #座標の面積公式を移行して，右辺をMの倍数になるように調整
        x1y2=M-S%M
        if S%M==0:
            x1y2=0
        x1=x1y2
        y2=1
        x2=10**9
        y1=(S+x1y2)//M
        print(0,0,x1,y1,x2,y2)


main()
