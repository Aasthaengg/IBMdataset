n=int(input())
l=list(map(int,input().split()))
cost=0
def diff(a,b):
    if a>b:
        return(a-b)
    else:
        return (b-a)
dp={}#i:j means min cost of going from i to 1 is j
dp[1]=0
dp[2]=diff(l[1],l[0])
for i in range(3,len(l)+1):
    dp[i]=min(diff(l[i-1],l[i-3])+dp[i-2],diff(l[i-1],l[i-2])+dp[i-1])
print(dp[n])
