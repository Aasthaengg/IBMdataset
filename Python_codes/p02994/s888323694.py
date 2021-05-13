n,l=map(int,input().split())
list=[]
for i in range(1,n+1):
  a=i+l-1
  list.append(a)
A=sum(list)
cnt=0
for i in list:
  if i<0:
    cnt+=1
if cnt==n:
  print(A-list[-1])
elif 0 in list:
  print(A)
elif cnt==0:
  print(A-list[0])