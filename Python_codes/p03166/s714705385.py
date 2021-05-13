from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
v,e=map(int,input().split())
m=defaultdict(list)

for i in range(e):
    x,y=map(int,input().split())
    m[x].append(y)
dp=defaultdict(lambda:-1)
def longestPath():
    
    def findLongestPath(vtx):
        if(dp[vtx]!=-1):
            return dp[vtx]
        res=0
        for i in m[vtx]:
            res=max(res,1+findLongestPath(i))
        dp[vtx]=res
        return res
        
        
    
    ans=0
    for i in range(1,v+1):
        ans=max(ans,findLongestPath(i))
    
    return ans;

print(longestPath())
