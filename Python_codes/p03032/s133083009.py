n,k=map(int,input().split())
*q,=map(int,input().split())

ans=0
for i in range(1,k+1): # iは抜き取り回数
    if i<n:
        for left in range(0,i+1): # 左からleft個目まで抜き取る
            tmp=0
            tmpq=[]
            right=i-left
            if right==0:
                right=-n
            tmpq+=q[:left]+q[-right:]
            tmp+=sum(tmpq)
            tmpq=[x for x in tmpq if x<0]
            tmpq=sorted(tmpq)
            tmp-=sum(tmpq[:min(k-i, len(tmpq))])
            ans=max(ans,tmp)
    else:
        for left in range(0,n+1):
            tmp=0
            tmpq=[]
            right=n-left
            if right==0:
                right=-n
            tmpq+=q[:left]+q[-right:]
            tmp+=sum(tmpq)
            tmpq=[x for x in tmpq if x<0]
            tmpq=sorted(tmpq)
            tmp-=sum(tmpq[:min(i-n, len(tmpq))])
            ans=max(ans,tmp)
print(ans)