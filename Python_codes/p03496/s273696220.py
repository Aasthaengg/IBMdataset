N=int(input())
alist=list(map(int,input().split()))

def isAsc(lst):
  for i in range(1,len(lst)):
    if lst[i-1]>lst[i]:
      return False
  else:
    return True

min_a=min(alist)
max_a=max(alist)

answer_list=[]
if max_a>0 and max_a>-min_a:
  while(not isAsc(alist)):
    desc_index=-1
    
    for i in range(1,N):
      if alist[i-1]>alist[i]:
        desc_index=i
        break
  
    max_a=-10**9
    max_index=-1
    for i in range(N):
      if alist[i]>max_a:
        max_a=alist[i]
        max_index=i    
      
    while(alist[desc_index-1]>alist[desc_index]):
      alist[desc_index]+=max_a
      answer_list.append((max_index+1,desc_index+1))
else:
  while(not isAsc(alist)):
    desc_index=-1
    
    for i in reversed(range(1,N)):
      if alist[i-1]>alist[i]:
        desc_index=i-1
        break
  
    min_a=10**9
    min_index=-1
    for i in range(N):
      if alist[i]<min_a:
        min_a=alist[i]
        min_index=i    
      
    while(alist[desc_index]>alist[desc_index+1]):
      alist[desc_index]+=min_a
      answer_list.append((min_index+1,desc_index+1))

#print(answer_list)
print(len(answer_list))
for x,y in answer_list:
  print(x,y)