n=int(input())
p=list(map(int,input().split()))
count=0
flag=False
for i in range(len(p)):
  if (i+1)==p[i]:
    count+=1
    if flag==True:
      count-=1
      flag=False
    else:
      flag=True
  else:
    flag=False
print(count)