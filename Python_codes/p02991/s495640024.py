def main():
    n,m=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in [0]*m]
    g=[[] for _ in [0]*n]
    [g[a-1].append(b-1) for a,b in ab]
    s,t=map(int,input().split())
    visit=[[False]*3 for _ in [0]*n]
    s-=1
    t-=1
    visit[s][0]=True
    cnt=0
    q=[s]
    while q:
        qq=[]
        cnt+=1
        c=cnt%3
        for i in q:
            for j in g[i]:
                if visit[j][c]==False:
                    visit[j][c]=True
                    qq.append(j)
        q=qq
        if visit[t][0]:
            print(cnt//3)
            break
    else:
        print(-1)
main()