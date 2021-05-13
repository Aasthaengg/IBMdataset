[h,w] = [int(i) for i in input().split()]
mod = 10**9+7
a = [["#"]*(w+2)]
for i in range(h):
    tmp = ["#"]
    s = input()
    for j in range(w):
        tmp.append(s[j])
    tmp.append("#")
    a.append(tmp)
a.append(["#"]*(w+2))

dp = [[0]* (w+2) for i in range(h+2)]
addi = 1
for i in range(1,h+1):
    if a[i][1] == "#":
        addi = 0
    dp[i][1] += addi
addi = 1
for i in range(2,w+1):
    if a[1][i] == "#":
        addi = 0
    dp[1][i] += addi


for i in range(2,h+1):
    for j in range(2,w+1):
        if a[i][j] != "#":
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= mod
print(dp[h][w])
#for i in range(h+2):
#    print(dp[i])
