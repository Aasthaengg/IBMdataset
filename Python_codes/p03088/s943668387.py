N = int(input())
dp = [[0 for _ in range(4**4)] for _ in range(N-3)]
cau = [6, 9, 24, 25, 26, 27, 33, 36, 37, 38, 39, 41, 45, 57, 70, 73, 97, 132, 133, 134, 135, 137, 161, 198, 201, 225]
if N==3:
    print(61)
    exit()

for i in range(4**4):
    dp[0][i] = 1 - cau.count(i)
for i in range(N-4):
    for j in range(4**4):
        if j in cau:
            dp[i+1][j] = 0
            continue
        tgt = 4*(j%(4**3))
        tgt_list = [tgt+i for i in range(4) if tgt+i not in cau]
        for elem in tgt_list:
            dp[i+1][j] += dp[i][elem]
        dp[i+1][j] = dp[i+1][j]%(10**9+7)
print(sum(dp[N-4])%(10**9+7))
"""
# calc cau
res = [[] for _ in range(8)]
for j in range(4**4):
    j1 = j//(4**3)
    j2 = j%(4**3)//(4**2)
    j3 = j%(4**2)//4
    j4 = j%4
    #res = 0
    if j2==0 and j3==2 and j4==1:
        res[0].append(j)
    if j1==0 and j3==2 and j4==1:
        res[1].append(j)
    if j1==0 and j2==2 and j4==1:
        res[2].append(j)
    if j2==2 and j3==0 and j4==1:
        res[3].append(j)
    if j2==0 and j3==1 and j4==2:
        res[4].append(j)
    if j1==0 and j2==2 and j3==1:
        res[5].append(j)
    if j1==2 and j2==0 and j3==1:
        res[6].append(j)
    if j1==0 and j2==1 and j3==2:
        res[7].append(j)
print(res)
"""
