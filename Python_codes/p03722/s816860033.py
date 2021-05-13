import sys
input=sys.stdin.readline  #危険！基本オフにしろ！


def BELLMANFORD(point,n,d):
    cost=[1e18]*(n+1)
    cost[point]=0
    for i in range(n-1):
        for (nownode,nextnode,c) in d:
            if cost[nextnode]>cost[nownode]+c:  #infが定数なので論理が逆
                cost[nextnode]=cost[nownode]+c
    for (nownode,nextnode,c) in d:
        if cost[nextnode]>cost[nownode]+c:
            if nextnode==n:
                return "inf"
            cost[nextnode]=cost[nownode]+c
            
    return -cost[n]


def main():
    n,m=map(int,input().split())
    
    d=[]
    for i in range(m):
        a,b,c=map(int,input().split())
        d.append((a,b,-c))
    
    print(BELLMANFORD(1,n,d))


if __name__ == '__main__':
    main()
