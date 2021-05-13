N, x = map(int, input().split())
a = sorted(map(int, input().split()))
      
count=0
for i in range(N):
  x=x-a[i]
  if x>=0:
    count+=1
  
if x>0:
  count-=1
  
print(count)