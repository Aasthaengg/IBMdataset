H,N =[int(i) for i in input().split()]
AAA = []
BBB = []
for i in range(N):
    buff = [int(i) for i in input().split()]
    AAA.append(buff[0])
    BBB.append(buff[1])

#dp[i]は体力をi減らすまでに必要な魔力の最小値
dp = [10000000000 for i in range(H+5)]
dp[0] = 0
for i in range(H+5):
    for j in range(N):
        A = AAA[j]
        B = BBB[j]
        if i-A>=0:
            dp[i]=min(dp[i],dp[i-A]+B)
        else:
            dp[i]=min(dp[i],B)

#print(dp)
print(dp[H])


