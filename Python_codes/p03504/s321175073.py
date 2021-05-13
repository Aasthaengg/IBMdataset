from collections import defaultdict
N,C=map(int,input().split())

event_list=[]
for i in range(N):
  s,t,c=map(int,input().split())
  event_list.append((s-0.5,c))
  event_list.append((t,-c))
event_list.sort()
#print(event_list)

answer=0
cdic=defaultdict(int)
for t,c in event_list:
  if c>0:
    cdic[c]+=1
    answer=max(answer,len(cdic))
  else:
    cdic[-c]-=1
    if cdic[-c]==0:
      cdic.pop(-c)
  #print(cdic)

print(answer)