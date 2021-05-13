n=int(input())
max_n=1
max_c=0

for i in range(n+1):
  c=0
  num=i
  while True:
    if num/2==0:
      break
      
    if num%2==0:
      c+=1
      num=num/2     
    else:
      break
      
  if c > max_c:
    max_c=c
    max_n=i
    
print(max_n)