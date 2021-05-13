n=int(input())
a=list(map(int,input().split()))
lis=[0]*9
for num in a:
    lis[min(8,num//400)]+=1
kind=0
for i in range(8):
    if lis[i]>0:
        kind+=1
if kind==0:
    mini=1
else:
    mini=kind
maxi=kind+lis[8]
print(mini,maxi)
#print(lis)