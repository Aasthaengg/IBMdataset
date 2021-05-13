n,k = [int(j) for j in input().split()]
l = [int(j) for j in input().split()]
dp = {0:False}
for j in range(1,k+1):
    flag  =True
    for i in l:
        if j-i>-1:
            if not dp[j-i]:
                dp[j] = True
                flag =False
                break
    if flag:
        dp[j] = False
if dp[k]:
    print("First")
else:
    print("Second")    