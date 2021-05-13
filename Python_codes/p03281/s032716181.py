N=int(input())
count=0
answer=0
for i in range(N):
  for j in range(i+1):
    if (i+1)%(j+1)==0:
      count+=1
  if count==8 and (i+1)%2==1:
    answer+=1
  count=0
print(answer)