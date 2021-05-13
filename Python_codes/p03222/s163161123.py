H,W,K=map(int,input().split())

#横棒設置可能箇所（目的とする縦棒に関与しない）がi本であるときに，横棒を置ける通り数
a=[1]*max((W-1),1)
for i in range(W-1):
    a[i]+=i#横線を1本引く
    if i-2>0:#2本引く
        a[i]+=((i-1)*(i-2))//2
        if i==5:#3本引く
            a[i]+=1
        elif i==6:#3本引く*4パターン
            a[i]+=4
    
mod=10**9+7    

#高さiまででj番目の通り数
dp=[[0]*W for _ in range(H+1)]
dp[0][0]=1#高さ0では1に行けるのが1通り

for i in range(H):
    for j in range(W):
        for k in range(-1,2,1):#両隣+自身
            if j+k>=0 and j+k<W:
                l=min(j,j+k)
                r=max(j,j+k)
                dp[i+1][j+k]+=dp[i][j]*a[max(0,l-1)]*a[max(0,(W-1)-r-1)]#通り数*左の冗長*右の冗長
                dp[i+1][j+k]%=mod
                
print(dp[-1][K-1])

