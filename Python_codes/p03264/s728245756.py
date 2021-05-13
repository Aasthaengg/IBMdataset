K = int(input())
res = 0
for i in range(1,K+1):
  if i % 2 == 0:
    for j in range(i+1,K+1):
      if j%2 !=0:
        res+=1
  else:
    for j in range(i+1,K+1):
      if j%2 ==0:
        res+=1
        
print(res)