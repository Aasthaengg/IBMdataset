n,k = [int(x) for x in input().split()]

arr  = [int(x) for x in input().split()]

# dp[i] -> having i stones in pile, True if player A can win starting from here

dp = [False]*(k+1)

dp[0] = False


for i in range(1,k+1):
    for e in arr:
        if i - e < 0:
            dp[i] = False
            break
        if dp[i-e] == False:
            dp[i] = True
            break

# print(dp)
if dp[k]:
    print('First')
else:
    print('Second')