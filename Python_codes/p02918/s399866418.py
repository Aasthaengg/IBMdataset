b=input().split()
K=int(b[1])
a=input()
count=0
for  i in range(len(a)) :
  if i!=len(a)-1 and a[i]=='R' and a[i+1]=='R':
    count+=1
  elif i!=0 and a[i]=='L' and a[i-1]=='L' :
    count+=1
    
for i in range(K) :
  count+=2

if count>=len(a)-1 :
  print(len(a)-1)
else :
  print(count)
