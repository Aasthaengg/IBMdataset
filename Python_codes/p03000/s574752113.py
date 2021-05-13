a,b=map(int,input().split())
list=list(map(int,input().split()))
 
count=0
count2=1
for i in range(a):
  count+=list[i]
  if count<=b:
    count2+=1
    
print(count2)
