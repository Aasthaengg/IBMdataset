k,s = map(int,input().split())

ans = 0
if(s == 0):
  print(1)
  exit()
elif(s == 3*k):
  print(1)
  exit()
  
for i in range(0,k+1):
  for j in range(0,k+1):
    z = s - i - j
    if(z >= 0 and z <= k):
      ans += 1
        
print(ans)