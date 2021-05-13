import math
n=int(input())
ans=n
for i in range(n):
    num=math.sqrt(ans)
    if num%1==0:
        break
    ans-=1
print(ans)
