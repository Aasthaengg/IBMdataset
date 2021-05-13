S = input()+'T'
X,Y = map(int,input().split())

xmove = []
ymove = []

tmp = 0
flag = True
for i in range(len(S)):
    if S[i]=='F':
        tmp += 1
    elif flag and S[i]=='T':
        xmove.append(tmp*2)
        tmp = 0
        flag = False
    else:
        ymove.append(tmp*2)
        tmp = 0
        flag = True
        
if xmove:
    x0 = xmove.pop(0)//2
else:
    x0 = 0

xgoal = sum(xmove)//2+X-x0
ygoal = sum(ymove)//2+Y

def subsetsum(arr,s):
    if not arr or s < 0:
        if s==0:
            return True
        else:
            return False
    dp = [[0 for j in range(s+1)] for i in range(len(arr)+1)]
    dp[0][0] = 1
    for i in range(1,len(arr)+1):
        for j in range(s+1):
            if j-arr[i-1]>=0:
                dp[i][j] = (dp[i-1][j-arr[i-1]] | dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][s]
    
if subsetsum(xmove,xgoal) and subsetsum(ymove,ygoal):
    print('Yes')
else:
    print('No')