x,y=map(int,input().split())
import bisect as bi
ans=1
for i in range(80):
    if x*2<=y:
        ans+=1
        x*=2
print(ans)