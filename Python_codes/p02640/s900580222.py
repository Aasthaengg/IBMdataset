n,t = list(map(int,input().split()))
 
m = 0
while m < n+1:
  if m*4 + (n-m)*2 == t:
    print('Yes')
    break
      
  m += 1
    
if m == (n+1):
  print('No')