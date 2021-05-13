import math
a,b=map(int,input().split())
r_max=int((b+1)//0.1)
r_min=int(b//0.1)
ans=0
for i in range(r_max,r_min,-1):
    if math.floor(i*0.08)==a:
        ans=i
print(-1 if ans==False else ans)