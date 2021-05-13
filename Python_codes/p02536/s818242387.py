def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    from collections import deque
    n,m=map(int,input().split())
    ab=[[] for _ in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        ab[a-1].append(b-1)
        ab[b-1].append(a-1)
    visit=[False]*n
    cnt=0
    while False in visit:
        for i in range(n):
            if visit[i]==True:
                continue
            cnt+=1
            q=deque()
            q.append(i)
            while q:
                x=q.popleft()
                visit[x]=True
                for nx in ab[x]:
                    if visit[nx]==True:
                        continue
                    q.append(nx)
    print(cnt-1)            

if __name__ == '__main__':
    resolve()