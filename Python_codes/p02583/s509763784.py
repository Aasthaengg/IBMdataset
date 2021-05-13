import itertools
 
N=int(input())
L=list(map(int,input().split()))

count=0

if len(L)<3:
    Lis=[]
else:
    Lis=list(itertools.combinations(L,3))
 
numb=len(Lis)

for i in range(numb):
    if len(L)<3:
        break
 
    if Lis[i][0]==Lis[i][1] or Lis[i][0]==Lis[i][2] or Lis[i][1]==Lis[i][2]:
        pass
    else:
        bpc=Lis[i][1]+Lis[i][2]
        bmc=abs(Lis[i][1]-Lis[i][2])
        if bmc<Lis[i][0] and Lis[i][0]<bpc:
            #if Lis[i][0]<bpc:
            count+=1
 
print(count)