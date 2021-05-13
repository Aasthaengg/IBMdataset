n,h=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a_i,b_i=map(int,input().split())
    a.append(a_i)
    b.append(b_i)

import bisect,math


b=sorted(b)
index = bisect.bisect_left(b,max(a))

cnt=0
for i in range(n-1,-1,-1):
    if i>=index:
        h-=b[i]
        cnt+=1
    else:
        break
    
    if h<=0:
        h=0
        break

ans=math.ceil(h/max(a))+cnt

print(ans)
