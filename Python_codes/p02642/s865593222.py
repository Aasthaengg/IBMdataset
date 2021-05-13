n=int(input())
a=list(map(int,input().split()))
num=[0]*(max(a)+1)
maxa=max(a)
cnt=1

for i in a:
  while 1:
    try:
      num[i*cnt]+=1
      cnt+=1
      
      
    except IndexError:
      break
  cnt=1      

count=0

for i in range(n):
  if num[a[i]]==1:
    count+=1
    
print(count)