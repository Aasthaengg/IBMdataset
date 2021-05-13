# ABC61 D - Score Attack  preference付

import sys
input=sys.stdin.readline  #危険！基本オフにしろ！

def BELLMANFORD(point,n,d):
    cost       = [-float("inf")]*(n+1)
    preference = [None         ]*(n+1)      #最適路のこと 
    cost[point]= 0
    for i in range(n-1):                                  #経路の長さは最大n-1であるため
        for nownode,nextnode,c in d:
            if cost[nextnode]<cost[nownode]+c:
                cost[nextnode]=cost[nownode]+c
                preference[nextnode]=nownode

    negative=[0]*(n+1)                                        #負閉路の長さは最大nであるため
    
    for i in range(n):                  #閉路判定
        for nownode,nextnode,c in d:
            if negative[nownode]:
                negative[nextnode]=1
            if cost[nextnode]<cost[nownode]+c:
                cost[nextnode]=cost[nownode]+c
                preference[nextnode]=nownode
                negative[nownode]=1
 
    return cost,negative


def main():
    n,m=map(int,input().split())
    
    d=[tuple(map(int,input().split()))for i in [0]*m]
    
    x,y=(BELLMANFORD(1,n,d))
    
    if y[n]:
        print("inf")
    else:
        print(x[n])


if __name__ == '__main__':
    main()
