import collections
n=int(input())
a=map(int,input().split())
b=list(collections.Counter(a).items())
lst=[]
Lst=[]
for i in range(len(b)):
  if b[i][1]>1:
    lst.append(int(b[i][0]))  
    if b[i][1]>3:
      Lst.append(int(b[i][0]))
if len(lst)<2 and len(Lst)==0:
  print(0)
else:
  if len(lst)==1:
    Lst.sort(reverse=True)
    print(Lst[0]**2)
  else:
    if len(Lst)>0:
      lst.sort(reverse=True)
      Lst.sort(reverse=True)
      print(max(lst[0]*lst[1],Lst[0]**2))     
    else:
      lst.sort(reverse=True)
      print(lst[0]*lst[1])
  
