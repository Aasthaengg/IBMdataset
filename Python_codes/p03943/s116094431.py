a=list(map(int,input().split()))
max=-1000000
i=0
rit=0
for x in a:
    if max<x:
        max=x
for x in a:
    i=i+x
rit=i-max
if max==rit:
    print('Yes')
else:
    print('No')
