import math
a,b=map(int,input().split())
ans=[]
for i in range(1251):
    if math.floor(i*0.08)==a and math.floor(i*0.1)==b:
        ans.append(i)
if len(ans)!=0:
    print(min(ans))
else:
    print("-1")
