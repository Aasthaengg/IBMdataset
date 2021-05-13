import sys
H,W=map(int,input().split())
a = [[c for c in l.strip()] for l in sys.stdin]
#print(a)
dic={}
for i in range(H):
  for j in range(W):
    if(a[i][j] not in dic):
      dic[a[i][j]]=1
    else:
      dic[a[i][j]]+=1
#print(dic)
flag=True
if(H%2==0 and W%2==0):
  for i in dic.keys():
    if(dic[i]%4!=0):
      flag=False
elif((H%2==1 and W%2==0)):
  count=0
  for i in dic.keys():
    if(dic[i]%2!=0):
      flag=False
    if(dic[i]%4==2):
      count+=1
  if(count>W//2):
    flag=False
elif((H%2==0 and W%2==1)): 
  count=0
  for i in dic.keys():
    if(dic[i]%2!=0):
      flag=False
    if(dic[i]%4==2):
      count+=1
  if(count>H//2):
    flag=False
else:
  count2=0
  count1=0
  for i in dic.keys():
    if(dic[i]%4==1):
      count1+=1
    elif(dic[i]%4==2):
      count2+=1
    elif(dic[i]%4==3):
      count1+=1
      count2+=1
  if(count1>2 or count2>(W+H)//2-1):
    flag=False
if flag:
  print("Yes")
else:
  print("No")