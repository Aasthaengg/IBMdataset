import sys
input=sys.stdin.readline

def main():
    n=int(input())
    XY=[tuple(map(int,input().split())) for _ in range(n)]
    U,V=[],[]
    for x,y in XY:
        U.append(x+y)
        V.append(x-y)
    print(max(max(U)-min(U),max(V)-min(V)))
    
if __name__=='__main__':
    main()