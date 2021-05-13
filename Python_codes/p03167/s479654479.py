

H, W = map(int, input().split())
arr = ['']*H
for i in range(H):
    arr[i] = input()
 
#print(arr)
dp = [[0]*W for _ in range(H)]

# arr =[
# ['.','.'],
# ['#','.'],
# ['.','.'],
# ['.','#'],
# ['.','.']
# ]








flag= False
#print(arr)
for h in range(H-1,-1,-1):
    #print(h,W-1)

    if arr[h][W-1]=='#':
        dp[h][W-1]=0
        flag =  True
    if flag:
        dp[h][W-1]=0
    else:
        dp[h][W-1]=1
#print(dp)
    
flag = False
for w in range(W-1,-1,-1):
    #print(h,W-1)
    if arr[H-1][w]=='#':
        dp[H-1][w]=0
        flag =  True
    if flag:
        dp[H-1][w]=0
    else:
        dp[H-1][w]=1


#print(dp)

MOD = 10**9+7

dp[H-1][W-1]=0

for row in range(H-1,0,-1):
    for col in range(W-1,0,-1):
        if arr[row-1][col-1]=='#':
            dp[row-1][col-1]=0
        elif dp[row][col-1] ==0 or dp[row-1][col]==0:
            dp[row-1][col-1] = max(dp[row][col-1],  dp[row-1][col])
            dp[row-1][col-1]%=MOD

        elif dp[row][col-1] > 0 and dp[row-1][col]>0:
            dp[row-1][col-1] = dp[row][col-1] +  dp[row-1][col]
            dp[row-1][col-1]%=MOD
        elif  dp[row][col-1] == 0 and dp[row-1][col] == 0:
            dp[row-1][col-1]==0


print(dp[0][0])



            
    
