x,y = map(int,input().split())
count = 1
while True:
  x = 2*x
  if x <= y:
    count+=1
  else:
    break
    
print(count)