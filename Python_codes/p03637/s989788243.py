n=int(input())
a=list(map(lambda x:int(x),input().split()))
cnt=0
cnt2=0
for i in a:
    if i%4==0:
        cnt+=1
    if i%4!=0 and i%2==0:
        cnt2+=1
if (2*cnt+cnt2>=n and cnt2>0) or (cnt2==0 and 2*cnt+1>=n):
    print('Yes')
else:
    print('No')
