def main():
    n=int(input())
    a=[list(map(int,input().split())) for _ in [0]*n]
    m=(n*(n-1))//2
    d=dict()
    dr=[]
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            d[(i,j)]=cnt
            dr.append((i,j))
            cnt+=1
    #print(d)
    #print(dr)
    g=[[] for _ in [0]*m]
    gr=[0]*m
    for i in range(n):
        temp=[]
        for j in a[i]:
            j-=1
            if i>j:temp.append(d[(j,i)])
            else:temp.append(d[(i,j)])
        for j in range(len(temp)-1):
            g[temp[j]].append(temp[j+1])
            gr[temp[j+1]]+=1
    #print(g)
    #print(gr)
    q=[]
    for i in range(m):
        if gr[i]==0:
            q.append(i)
    cnt=0
    #print(q)
    while q:
        cnt+=1
        qq=[]#次回に回す分
        temp=[]#今回試合する分
        s=set()#戦うチーム
        while q:#今回の試合を抽出
            i=q.pop()
            x,y=dr[i]
            if (x not in s) and (y not in s):
                temp.append(i)
                s.add(x)
                s.add(y)
            else:
                qq.append(i)
        #print(temp,"t")
        while temp:
            i=temp.pop()
            for j in g[i]:
                gr[j]-=1
                if gr[j]==0:
                    qq.append(j)
        #print(qq)
        q=qq
    if sum(gr)==0:
        print(cnt)
    else:
        print(-1)



main()