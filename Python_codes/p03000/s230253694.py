N, val= list(map(int,input().split()))
list = list(map(int,input().split()))
d=0
l=[]
for i in list:
  d=d+i
  l.append(d)
count=0
for num in l:
  if num<=val:
    count=count+1
print(count+1)