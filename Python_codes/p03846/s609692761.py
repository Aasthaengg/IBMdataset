n=int(input())
numlist=list(map(int,input().split()))
num=[]
for i in range(n):
  num.append(0)
count=0
for i in numlist:
  num[i]+=1
  if num[i]==3:
    count=-1
    break
  elif i==0 and num[0]==2:
    count=-1
    break
  else:
    pass
if count==-1:
  print(0)
else:
  count=2**(n//2)
  count=count%(10**9+7)
  print(count)