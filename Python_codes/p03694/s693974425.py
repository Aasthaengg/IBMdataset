input()
lis=list(map(int,input().split()))
lis.sort()
dist=0
begin=lis[0]
for a in lis:
    dist+=a-begin
    begin=a
print(dist)