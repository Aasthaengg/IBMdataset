def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    import sys
    input = sys.stdin.readline
    H,W,m=map(int,input().split())
    bomb=set()
    cnt1=[0 for i in range(H)]
    cnt2=[0 for i in range(W)]
    for i in range(m):
        h,w=map(int,input().split())
        bomb.add((h-1,w-1))
        cnt1[h-1]+=1
        cnt2[w-1]+=1
    m1=max(cnt1)
    m2=max(cnt2)
    hk,wk=[],[]
    for i,x in enumerate(cnt1):
        if x==m1:
           hk.append(i)
    for i,x in enumerate(cnt2):
        if x==m2:
           wk.append(i)
    ans=m1+m2
    for i in hk:
        for j in wk:
            if (i,j) in bomb:
                continue
            print(ans)
            exit()
    print(ans-1)

if __name__ == '__main__':
    resolve()