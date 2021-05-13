import math
a,b,c = map(int,input().split())
d = list(map(int,input().split()))
ans = 0
for i in range(a):
    sum = c
    e = list(map(int,input().split()))
    for j in range(b):
        sum += e[j]*d[j]
    if sum>0:
        ans+=1

print(ans)