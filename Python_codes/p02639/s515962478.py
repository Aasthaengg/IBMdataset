books1= list(map(int, input().split()))
i=0
while(i<len(books1)):
  if(books1[i]==0):
    break
  i+=1
print(i+1)
