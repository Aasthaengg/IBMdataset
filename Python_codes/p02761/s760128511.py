def readinput():
    n,m=map(int,input().split())
    sc=[]
    for _ in range(m):
        s,c=map(int,input().split())
        sc.append((s,c))
    return n,m,sc

def main(n,m,sc):
    ans=[-1]*n
    for s,c in sc:
        if ans[s-1]==-1:
            ans[s-1]=c
        else:
            if ans[s-1]!=c:
                return -1
    if ans[0]==0:
        if n==1:
            return 0
        else:
            return -1
    elif ans[0]==-1:
        if n==1:
            ans[0]=0
        else:
            ans[0]=1
    for i in range(1,n):
        if ans[i]==-1:
            ans[i]=0
    sum=0
    for i in range(n):
        sum*=10
        sum+=ans[i]
    return sum

if __name__=='__main__':
    n,m,sc=readinput()
    ans=main(n,m,sc)
    print(ans)
