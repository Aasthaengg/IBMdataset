a,b,c=list(map(int,input().split()))
count=0
while(a<=b):
  b-=a
  if count==c:
    break
  count+=1
print(count)