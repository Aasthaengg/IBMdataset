n= list(map(int,input().split()))

count = 0
for i in range(n[0]):
  next = i + (n[1]-1)
  # print(i, next, n[0])
  if(next >= n[0]):
    break
    
  count += 1
  
print(count)