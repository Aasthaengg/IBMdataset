import sys
input=sys.stdin.readline  #危険！基本オフにしろ！

def BELLMANFORD(point,d,n):
    cost       = [-float("inf")for node in range(n+1)]
    cost[point]= 0
    for i in range(n-1):                                  #経路の長さは最大n-1であるため
        for now,lis in d.items():
            for nex,c in lis:
                if cost[nex]<cost[now]+c:
                    cost[nex]=cost[now]+c

    negative=[0]*n                                        #負閉路の長さは最大nであるため
    
    for i in range(n):                  #閉路判定
        for now,lis in d.items():
            for nex,c in lis:
                if negative[now-1]==1:
                    negative[nex-1]=1
                if cost[nex]<cost[now]+c:
                    cost[nex]=cost[now]+c
                    negative[now-1]=1
 
    return cost,negative


def main():
    n,m=map(int,input().split())
    
    d={}
    for s in range(m):
        a,b,c=map(int,input().split())
        if a in d:
            d[a].append((b,c))
        else:
            d[a]=[(b,c)]
    
    x,y=(BELLMANFORD(1,d,n))
    
    if y[n-1]>0:
        print("inf")
    else:
        print(x[n])


if __name__ == '__main__':
    main()
