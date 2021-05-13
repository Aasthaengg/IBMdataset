n,k=map(int,input().split())
lst=list(map(int,input().split()))
import math
p=len(lst)
p-=k
ans=1
ans+=math.ceil(p/(k-1))
print(ans)