h=int(input())
count=1
ans=0
while h>1:
  h=h//2
  count+=1 
for i in range(1,count+1):
  ans+=2**(i-1)
print(ans)