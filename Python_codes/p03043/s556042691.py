n,k=map(int, input().split())
ans=0
import math
for i in range(1,n+1):
    sikou=math.ceil(math.log((k/i),2))
    if sikou<0:
        sikou=0
    ans+=(1/n)*0.5**sikou
print(ans)