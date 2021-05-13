x,y=map(int,input().split())

cnt=0

for i in range(x+1):
    if 2*i+4*(x-i)==y:
        cnt+=1

if cnt==0:
    print('No')
else:
    print('Yes')
