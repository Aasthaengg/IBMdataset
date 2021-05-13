k, s=map(int, input().split())
count=0
for x in range(k+1):
  for y in range(k+1):
    z=s-x-y
    if k>=z>=0:
      count+=1
print(count)