#A
import copy

s=list(input())
times=[0]*26

ans=float('inf')


for i in s:
  temp=copy.deepcopy(s)
  tempans=0
  while True:
    #print(i,temp.count(i), len(temp))
    if temp.count(i)==len(temp):
      ans=min(ans,tempans)
      break
    else:
      for j in range(len(temp)-1):
        if temp[j+1]==i:
          temp[j]=i
      tempans+=1
      del temp[-1]
      #print(temp,tempans)
      
print(ans)