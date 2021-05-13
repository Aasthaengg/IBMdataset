import math
n = int(input())
p = list((map(int,input().split())))
ch = 0
ans = 0
for i in range(n):
    if p[i]==i+1:
        ch+=1
    if p[i]!=i+1:
        if ch ==1:
            ans+=1
        if ch >1:
            ans+=math.ceil(ch/2)
        ch = 0
if ch ==1:
    ans+=1
if ch >1:
    ans+=math.ceil(ch/2)
print(ans)
