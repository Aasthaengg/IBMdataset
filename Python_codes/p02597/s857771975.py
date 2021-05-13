n=int(input())
c=list(input())

import math

rkosu=c.count("R")
wkosu=n-rkosu

ca=["R"]*rkosu+["W"]*wkosu

count=0
for i in range(n):
    if c[i] != ca[i]:
        count+=1

ans=math.ceil(count/2)
print(ans)