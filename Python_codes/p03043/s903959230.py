N,K=map(int,input().split())

import math
ans=0
for i in range(1, N+1):
    ans+=1/N*(1/2)**max(0,-(-math.log2(K/i)//1))
    #print(i,ans, -(-math.log2(K/i)//1))

print(ans)