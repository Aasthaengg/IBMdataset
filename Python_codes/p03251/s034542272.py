import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        n,m,x,y=map(int, input().split())
        lx=list(map(int,input().split()))
        ly=list(map(int,input().split()))
        xmax=max(lx)
        ymin=min(ly)
        for i in range(x+1,y+1):
            if xmax<i and ymin >=i:
                return 'No War'
        return 'War'
    print(main())
resolve()