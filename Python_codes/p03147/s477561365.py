n,ans,now = int(input()),0,0
h = list(map(int,input().split()))
for i in range(n):
    if now<h[i]: ans+=h[i]-now
    now = h[i]
print(ans)