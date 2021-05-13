h,w,k=map(int,input().split())
mod=10**9+7
dp=[[0]*w for _ in range(h+1)] #dp[i][j]:=端点iまで辺を張った時辺ｊにたどり着くあみだくじの数
dp[0][0]=1
for hi in range(1,h+1):
    for i in range(2**(w-1)):
        idx1=[]
        idx2=[]
        ok=True
        for j in range(w-1):
            if (i>>j)&1:
                idx1.append(j)
                idx2.append(j)
                idx2.append(j+1)
        if len(idx1)>=2:
            for j in range(len(idx1)-1):
                if idx1[j+1]==idx1[j]+1:
                    ok=False
        if not ok:
            continue
        idx1=set(idx1)
        idx2=set(idx2)
        for wi in range(w):
            if wi in idx1:
                dp[hi][wi]+=dp[hi-1][wi+1]
                dp[hi][wi+1]+=dp[hi-1][wi]
                dp[hi][wi]%=mod
                dp[hi][wi+1]%=mod
            if wi not in idx2:
                dp[hi][wi]+=dp[hi-1][wi]
                dp[hi][wi]%=mod
print(dp[h][k-1])