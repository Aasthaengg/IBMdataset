import math
n,k=map(int,input().split())
ans='NO'
if math.ceil(n/2)>=k:
    ans='YES'
print(ans)