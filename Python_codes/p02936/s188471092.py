def main():
    n,q=map(int,input().split())
    ab=[[] for _ in range(n)]
    for i in range(n-1):
        a,b=map(int,input().split())
        ab[a-1].append(b-1)
        ab[b-1].append(a-1)
    visit=[False]*n
    cnt=[0]*n
    for i in range(q):
        p,x=map(int,input().split())
        cnt[p-1]+=x
    q=[(0,0)]
    while q:
        v,a=q.pop()
        visit[v]=True
        a+=cnt[v]
        cnt[v]=a
        for i in ab[v]:
            if visit[i]:
                continue
            else:
                q.append((i,a))
    print(*cnt)

if __name__ == '__main__':
    main()