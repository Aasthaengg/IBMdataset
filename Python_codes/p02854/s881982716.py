n = int(input())
l = list(map(int,input().split()))

from itertools import accumulate

tot=sum(l)
ans=2020202020*100000
for i in list(accumulate(l)):
    if i <= tot//2:
        ans=min(ans, abs(tot-(i*2)))

for i in list(accumulate(l[::-1])):
    if i <= tot//2:
        ans=min(ans, abs(tot-(i*2)))

print(ans)