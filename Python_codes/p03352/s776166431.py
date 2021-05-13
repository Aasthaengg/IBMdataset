x = int(input())
if x == 1:
  print("1")
  exit()
  
ans = 0
for b in range(2,int(x**(1/2)+1)):
  for p in range(2,1000):
    tmp = pow(b,p)
    if tmp<=x:
      ans = max(ans,pow(b,p))
    else:
      break
      
print(ans)
