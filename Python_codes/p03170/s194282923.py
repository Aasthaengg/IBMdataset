n,k = map(int,input().split())
A = list(map(int,input().split()))
# 先手目線で考える。手元にj枚あって、勝てるならTrue
dp = [False]*(k+1)
for i in range(1,k+1):
    flag = False
    for j in range(n):
        if i-A[j] >= 0:
            if dp[i-A[j]] == False:
                flag = True
                break
    if flag:
        dp[i] = True
    else:
        dp[i] = False
if dp[k]:
    print('First')
else:
    print('Second')
