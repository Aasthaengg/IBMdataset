n=int(input())

#3<=N<=100

#i文字目がdの件数
#ACGT
mod=10**9+7
#NG
#AGC
#ACG
#GAC
#AGGC
#AGAC

index=[]
for s1 in "AGCT":
    for s2 in "AGCT":
        for s3 in "AGCT":
            for s4 in "AGCT":
                index.append(s1+s2+s3+s4)

#dp[i][bk]

dp=[[0]*256 for _ in range(n)]

if n==3:
    print(61)
    exit()
elif n==4:
    print(230)
    exit()

cnt=0
for i,item in enumerate(index):
    flag=0
    for ng in ["AGC","ACG","GAC","AGGC","ACGC","AGAC","ATGC","AGTC"]:
        if item==ng or item[1:]==ng or item[:-1]==ng:
            flag=1
    if flag==0:
        dp[3][index.index(item)]=1

for i in range(4,n):
    for j,item in enumerate(index):
        for s in "AGCT":
            ss=item[1:]+s
            flag=0
            for ng in ["AGC","ACG","GAC","AGGC","ACGC","AGAC","ATGC","AGTC"]:
                if ss==ng or ss[1:]==ng or ss[:-1]==ng:
                    flag=1
            if flag==0:
                dp[i][index.index(ss)]+=dp[i-1][j]%mod

print(sum(dp[-1])%mod)
