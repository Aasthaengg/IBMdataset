import sys
input = sys.stdin.readline

H,W,K = map(int,input().split())
mod = 1000000007
dp = [[0]*(W+2) for _ in range(H+1)]
dp[0][1]=1
for i in range(1,H+1):
    for j in range(1,W+1):
        x=0
        y=0
        z=0
        for k in range(2**(W-1)):
            tmp = format(k, "b")
            tmp = tmp.zfill(W-1)
            tmp += "0"
            tmp = list(tmp)
            Flag = True
            for l in range(len(tmp)-1):
                if tmp[l] == tmp[l+1] == "1" or (j>=2 and tmp[j-2] != "1"):
                    Flag = False
                    break
            if Flag:
                x+=1
        for k in range(2**(W-1)):
            tmp = format(k, "b")
            tmp = tmp.zfill(W-1)
            tmp += "0"
            tmp = list(tmp)
            Flag = True
            for l in range(len(tmp)-1):
                if tmp[l] == tmp[l+1] == "1" or (j>=2 and tmp[j-2] == "1") or (j>=1 and tmp[j-1] == "1"):
                    Flag = False
                    break
            if Flag:
                y+=1   
        for k in range(2**(W-1)):
            tmp = format(k, "b")
            tmp = tmp.zfill(W-1)
            tmp += "0"
            tmp = list(tmp)
            Flag = True
            for l in range(len(tmp)-1):
                if tmp[l] == tmp[l+1] == "1" or (j>=1 and tmp[j-1] != "1"):
                    Flag = False
                    break
            if Flag:
                z+=1   
        dp[i][j] += x*dp[i-1][j-1]+y*dp[i-1][j]+z*dp[i-1][j+1]
        dp[i][j] %= mod
print(dp[H][K]%mod)